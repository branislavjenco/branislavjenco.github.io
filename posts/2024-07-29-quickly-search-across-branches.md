---
Quickly search in the HEADs of all branches in git with PowerShell
July 29th, 2024
---

Using PowerShell, you can quickly search for a string in the HEADs of all branches in a git repository like this:

```git ls-remote --heads -q | % { git grep <your-string> $_.Split()[0] }```

The first command returns the hashes and names of all the heads of branches. We then iterate over this list, and pick out only the first part (the hash) to be used by the `git grep` command. `Split()[0]` works here kind of like an `xargs`.