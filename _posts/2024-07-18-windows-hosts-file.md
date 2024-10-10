---
layout: post
title: Check this if editing the etc\hosts file doesn't work properly on Windows
---

If you add an entry into the hosts file in Windows (path is `C:\Windows\System32\drivers\etc\hosts`) for the loopback address (`127.0.0.1`), but your domain mapping still doesn't work, try adding the IPv6 version as well (`::1`).

Like this:

```
127.0.0.1 example.com
::1 example.com
```
