---
layout: post
title: Hash-based partitioning of resources is useful for statistics
---

Hash-based partitioning of your resources allows you to work on small but representative samples of data when collecting statistics.

**Example:** Imagine you are building a database. You save files into cloud buckets and partition your files into many different buckets based on a hash of some relatively random independent variable that can be associated with each file. One can then take one of these buckets and do some statistics on it (how many files there are, how big they get, access patterns etc.) and get representative results for the whole cluster, without having to look at all the buckets.
