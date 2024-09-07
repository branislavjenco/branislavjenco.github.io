# 2024-07-29 How to quickly search for a string in the heads of all branches in a git repository with PowerShell
Using PowerShell, you can quickly search for a string in the heads of all branches in a git repository like this:
```
git ls-remote --heads -q | % { git grep <your-string> $_.Split()[0] }
```
The first command returns the hashes and names of all the heads of branches. We then iterate over this list, and pick out only the first part (the hash) to be used by the `git grep` command. `Split()[0]` here is kind of like a poor man's `xargs`.


# 2024-07-18 `etc\hosts` file not working properly on Windows
If you add an entry into the hosts file in Windows (path is `C:\Windows\System32\drivers\etc\hosts`) for the loopback address (`127.0.0.1`), but your domain mapping still doesn't work, try adding the IPv6 version as well (`::1`).
```
127.0.0.1 example.com
::1 example.com
```


# 2024-07-17 Fixing stuck SMB File Share in Azure
I had an issue with an SMB File Share in an Azure Storage Account stuck in an in-between state. The file share gets regularly deleted and created anew, and has a seven-day soft delete policy, meaning it has multiple deleted versions saved. At some point, maybe because of a Service Health event, the latest version of the file share was both _not present_ among the active file shares, but also _wasn't_ "deleted". Any operation on the file share returned a 404, including trying to delete it. Doing a `CreateIfNotExists` on the file share also failed. Hence, we were stuck.

Solution: Pick the next-to-last version from the deleted versions list, undelete it, and delete it again. The (new) last version is then correctly marked as "deleted" and `CreateIfNotExists` succeeds.


# 2024-06-19 Escaping dollar signs in PowerShell
In PowerShell, you have to use single quotes (`'`) to escape dollar signs (`$`) in a string. Double quotes won't do it. Alternatively escape particular `$` with a backtick in front (`` `$ ``). 


# 2024-06-10 .show in Azure Data Explorer
In Azure Data Explorer, you can use `.show` to look up interesting information about the [functions](https://learn.microsoft.com/en-us/azure/data-explorer/kusto/management/show-function), previous [commands and queries](https://learn.microsoft.com/en-us/azure/data-explorer/kusto/management/commands-and-queries) or [clusters](https://learn.microsoft.com/en-us/azure/data-explorer/kusto/management/show-cluster-database) when writing a query. Example: `.show cluster databases datastats` shows stats about original/compressed/index size of your databases.


# 2024-06-08 When in doubt, flush DNS
I had an interesting issue in Windows VM running in Azure, trying to connect to Storage Account A. From inside the VM I was unable to even resolve the storage account's public domain name, yet this was possible from my computer. I was able to resolve the domain name of Storage Account B. The difference in A and B is that B has a private endpoint defined, even though it's used for a completely different purpose. If I added a private endpoint to Storage Account B, I was able to resolve the public domain name from inside the VM. This makes sense, as is pointed out in the [docs](https://learn.microsoft.com/en-us/azure/storage/common/storage-private-endpoints#dns-changes-for-private-endpoints). But again, without this private link, I was unable to resolve the domain name from the VM, yet I was able to do so from my computer regardless. If I _removed_ the private endpoint, the resolution failed in the VM. This is all using the default DNS server, the issue doesn't happen if I use Google's. Finally, I tried `ipconfig /flushdns` on the VM, which fixed the issue.


# 2024-03-03 Hashased partitioning is useful for analysis
Hash-based partitioning of your storage allows you to work on small but representative samples of data when collecting statistics.