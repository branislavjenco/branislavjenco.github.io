---
Use .show in Azure Data Explorer
2024-06-10
---

In Azure Data Explorer, you can use `.show` to look up interesting information about the [functions](https://learn.microsoft.com/en-us/azure/data-explorer/kusto/management/show-function), previous [commands and queries](https://learn.microsoft.com/en-us/azure/data-explorer/kusto/management/commands-and-queries) or [clusters](https://learn.microsoft.com/en-us/azure/data-explorer/kusto/management/show-cluster-database) when writing a query. Example: `.show cluster databases datastats` shows stats about original/compressed/index size of your databases.