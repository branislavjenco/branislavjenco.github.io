---
layout: page
title: Today I learned
permalink: /til
---

## 2024-03-03
Hash-based partitioning of your storage allows you to work on small but representative samples of data when collecting statistics.

## 2024-06-08
When in doubt, flush DNS. I had an interesting issue in Windows VM running in Azure, trying to connect to Storage Account A. From inside the VM I was unable to even resolve the storage account's public domain name, yet this was possible from my computer. I was able to resolve the domain name of Storage Account B. The difference in A and B is that B has a private endpoint defined, even though it's used for a completely different purpose. If I added a private endpoint to Storage Account B, I was able to resolve the public domain name from inside the VM. This makes sense, as is pointed out in the [docs](https://learn.microsoft.com/en-us/azure/storage/common/storage-private-endpoints#dns-changes-for-private-endpoints). But again, without this private link, I was unable to resolve the domain name from the VM, yet I was able to do so from my computer regardless. If I _removed_ the private endpoint, the resolution failed in the VM. This is all using the default DNS server, the issue doesn't happen if I use Google's. Finally, I tried `ipconfig /flushdns` on the VM, which fixed the issue.

## 2024-06-10
In Azure Data Explorer, you can use `.show` to look up interesting information about the [functions](https://learn.microsoft.com/en-us/azure/data-explorer/kusto/management/show-function), previous [commands and queries](https://learn.microsoft.com/en-us/azure/data-explorer/kusto/management/commands-and-queries) or [clusters](https://learn.microsoft.com/en-us/azure/data-explorer/kusto/management/show-cluster-database) when writing a query. Example: `.show cluster databases datastats` shows stats about original/compressed/index size of your databases.

## 2024-06-19
In PowerShell you have to use single quotes (`'`) to escape dollar signs (`$`) in a string. Alternatively escape particular `$` with a backtick in front (`` `$ ``).
 
