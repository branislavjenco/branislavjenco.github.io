---
title: How to quickly search for a string in the heads of all branches in a git repository with PowerShell
---

Using PowerShell, you can quickly search for a string in the heads of all branches in a git repository like this:```git ls-remote --heads -q | % { git grep <your-string> $_.Split()[0] }```The first command returns the hashes and names of all the heads of branches. We then iterate over this list, and pick out only the first part (the hash) to be used by the `git grep` command. `Split()[0]` here is kind of like a poor man's `xargs`.