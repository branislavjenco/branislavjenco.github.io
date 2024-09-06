---
title: Containers using glibc v2.34+ don't work on some older docker versions 
---

After updating a docker image to use Ubuntu 22.04 as base (from 20.04), error messages started appearing when running containers, looking like this:

`error message in jemalloc <jemalloc>: arena 0 background thread creation failed (1)`

The docker image uses the [jemalloc](https://github.com/jemalloc/jemalloc) allocator, but as will be shown, it has nothing to do with this problem. This was happening only in certain environments - not in the Azure Kubernetes Service (AKS) and not on all hosts running regular `docker`. It seemed to apply to specifically some hosts running older versions of `docker`. The problem turned out to be the following:

That specific `jemalloc` error message [is a result of jemalloc failing to create a background thread](https://github.com/jemalloc/jemalloc/blob/54eaed1d8b56b1aa528be3bdd1877e59c56fa90c/src/background_thread.c#L500). `jemalloc` uses the [pthread_create](https://man7.org/linux/man-pages/man3/pthread_create.3.html) function of [glibc](https://www.gnu.org/software/libc/) which in turn uses a syscall called [clone](https://man7.org/linux/man-pages/man2/clone.2.html) to create child processes. 

Starting from the linux kernel version 5.3, released on September 15th 2019, a new version of the clone syscall was introduced, [clone3](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=8f6ccf6159aed1f04c6d179f61f6fb2691261e84). The new syscall provides a superset of the functionality of the older `clone` interface and a number of API improvements.

glibc [started using this new syscall optionally](https://patchwork.sourceware.org/project/glibc/patch/20210601145516.3553627-2-hjl.tools@gmail.com/) in its implementation of `pthread_create` in version [2.34](https://sourceware.org/glibc/wiki/Release/2.34). Importantly, Ubuntu 22.04 uses glibc 2.35, whereas Ubuntu 20.04 used glibc 2.31. This problem would happen on Ubuntu 21.10 as well, as it uses glibc 2.34 (Ubuntu 21.04 uses glibc 2.33). What it boils down to is that in Ubuntu 21.10 and 22.04, glibc tries to use the `clone3` syscall.

glibc implements this syscall in a wrapper which, if it returns with an ENOSYS ([Function not implemented](https://www.gnu.org/software/libc/manual/html_node/Error-Codes.html)) error code, falls back to the older `clone` implementation. This is where the other part of the story comes in. `docker` uses [seccomp](https://en.wikipedia.org/wiki/Seccomp) to disallow certain syscalls from being executed in the container. This filtering can be configured using [seccomp security profiles](https://docs.docker.com/engine/security/seccomp/) (or bypassed entirely by running containers in [privileged mode](https://docs.docker.com/engine/reference/run/#runtime-privilege-and-linux-capabilities)).

However, when the syscall filter mechanism in docker encountered a new syscall (`clone3`) it returned an EPERM (Operation not permitted) error code back instead of ENOSYS. This meant that glibc doesn't fall back to the older implementation and the syscall fails. 

`runc` added a "special handling for seccomp profiles to avoid making new syscalls unusable for glibc" already in [v1.0.0-rc93](https://github.com/opencontainers/runc/releases/tag/v1.0.0-rc93) ([this PR](https://github.com/opencontainers/runc/pull/2750)), but the fix is more of a [workaround](https://github.com/moby/moby/pull/42681#issuecomment-923434718) than a proper fix and seems to not always work. `runc` is the CLI tool used for spawning containers, which is used by `containerd`. `containerd` handles the lifecycle, networking and other aspects of containers, and is in turn used by `docker` itself (i recommend looking at [The differences between Docker, containerd, CRI-O and runc](https://www.tutorialworks.com/difference-docker-containerd-runc-crio-oci/) to understand how things hang together.) `runc` uses the [libseccomp](https://github.com/seccomp/libseccomp) library for the actual seccomp implementation (which is again a [syscall](https://man7.org/linux/man-pages/man2/seccomp.2.html)).

The support for `clone3` in the seccomp profile was added in [docker-ce 20.10.10](https://github.com/moby/moby/releases/tag/v20.10.10). If your docker is at least this version, this problem shouldn't happen. However, if your docker is older than this, you _might_ have this problem, but not necessarily. This is where the difference between `docker.io` and `docker-ce` comes in. `docker.io` is the older package used for distributing docker, and is maintained by Debian. It can be installed from the usual package repositories in Ubuntu/Debian. `docker-ce` is the Community Edition of docker, distribution by Docker (the company). For tradeoffs between these two, see [this discussion](https://stackoverflow.com/a/57678382). 

Importantly, the `docker.io` package used by Ubuntu contains a [patch that fixes this issue](https://git.launchpad.net/ubuntu/+source/containerd/commit/?id=452f02f704fd55a309b7c4618e72bdba1e491671) even for docker versions older than 20.10.10 (tested with v20.10.7). This patch and the general mess of versioning and backporting all the components inside docker, is what makes this problem tricky to figure out. 

In summary, make sure you are using docker v20.10.10 if using `docker-ce` or a patched older version if using `docker.io` when running images with glibc v2.34+.

Some other relevant discussions on github:
- [[20.10 backport] seccomp: add support for "clone3" syscall in default policy](https://github.com/moby/moby/pull/42836)
- [seccomp: add support for "clone3" syscall in default policy](https://github.com/moby/moby/pull/42681)





