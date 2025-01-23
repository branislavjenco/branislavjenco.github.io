---
layout: post
title: Don't be afraid of rabbit holes 
---

I've gotten myself into some deep rabbit holes in the course of everyday software development. I find some surprising behavior, or an apparent bug, and before I know it, 57 tabs are open in my browser. They hold a record of my journey through the source code of 5 different codebases, their GitHub Issues, their fork's GitHub Issues, Stack Overflow, paywalled Medium articles that weren't worth opening and, these days, a conversation with a helpful-but-not-really LLM. 

I probably found a way to solve the problem 46 tabs ago, but I couldn't let go until I understood exactly _why_, for example,  [Containers using glibc v2.34+ don't work on some older docker versions](https://blog.br4.no/docker-jemalloc-clone3/). The letting go part is tricky. Rabbit holes are often fractal, which is a problem. There's always something more to discover.

But I try to force myself to stop at some point. That point is usually around the place where I am not learning anything new about the underlying principles, and what's left are implementation details of the various systems involved. In other words, when I've acquired some insight that is somewhat timeless, and useful elsewhere.

When I was spelunking in the rabbit holes of [socket reuse in Linux and Windows](https://blog.br4.no/reusing-sockets), at some point I felt reasonably satisfied with my understanding and I let go. Going through the myriad of socket attribute combinations and their behaviour in Windows was not something I felt was worth my time. That is something I can always find again if needed.

Occasionally, when the rabbit hole isn't deep, I find the end of it, like when I encountered an [unintuitive behaviour in Python's `requests`](https://blog.br4.no/requests-iter_lines) package. Nothing is left unearthed and it feels good. A worse feeling is when I find that a problem is entirely self-inflicted, like when [forgetting to set up a NodeSelector in a local Kubernetes/kind environment](https://blog.br4.no/kubernetes-scheduling/). But the benefits are still there as I understood more about how Kubernetes works.

But if I learned something interesting today, I'm probably going to forget it in a couple of days. That's why I spend a little effort to write notes during my rabbit hole journeys and turn them into blog posts. You might have noticed the links in this post.

This doesn't happen every time, but honestly unless I do that, I am most likely going to forget about it. Writing a blog post creates a stronger association in my memory and I can always look it up later. Not to mention the obvious benefit to other programmers who find a blog post helpful in their own spelunking.

I encourage the reader to go and dive into your rabbit holes head-first. Just know when to stop, and blog about it! It helps you and it helps others.