---
layout: post
title: Intermittent networking issues in k8s and kind
---

We are using [`kind`](https://kind.sigs.k8s.io/) for local k8s development and CI testing. `kind` allows you to run a k8s cluster using docker containers as worker nodes which makes it quick to spin up and tear down an environment. We've been having an intermittent issue with the local dev environment as we started using [`helm`](https://helm.sh/docs/topics/charts/) charts for deployment of our application, where we could not talk to to an exposed [`NodePort`](https://kubernetes.io/docs/concepts/services-networking/service/#nodeport) service of the cluster. This service routes to a [Traefik](https://traefik.io/) instance running inside the cluster which then routes to our components.

Seemingly at random, requests from the host machine to the cluster would time out. The behaviour sometimes changed when we recreated the cluster, but not always. We thought it might be related to some different docker containers running on the machine and therefore port collisions, wrong port-forwarding setup in the cluster, bug in `kind` and many other possibilities.


The problem turned out incredibly trivial. We run 3 worker nodes in the cluster, which correspond to 3 docker containers when running a `kind` cluster. You have to specify `extraPortMapping` rules in the `kind` [configuration](https://kind.sigs.k8s.io/docs/user/configuration/#extra-port-mappings) to be able to to talk to them from the host machine. This was set up for the first of the 3 nodes.

The issue was that we were running only 1 instance of Traefik without any [nodeSelector](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/). This meant that everytime we spun up the cluster or restarted Traefik, the k8s scheduler made a new decision about which worker node to run it on. In our setup, this has basically meant at random. If it picked any but the first node (which had the port-forwarding setup), there would be no way for us to reach it from the host machine and our requests timed out. Before moving to Helm, we used to run 3 instances of Traefik in a `DeamonSet` so we didn't have this issue.


The lesson to learn here is that when you are debugging a seemingly randomly occuring issue in a k8s environment, double check your assumptions about how your pods are scheduled on the worker nodes. Especially when running in `kind` with another layer of port forwarding indirection added. See [Kubernetes Scheduler](https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/) for more information about pod scheduling.
