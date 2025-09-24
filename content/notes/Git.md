---
title: Git
date: 2024-09-24 09:46:50Z
updated: 2025-06-10 11:11:35Z
taxonomies:
  tags:
  - linux
---

### Merge Strategies

If there're too many conflicts, and you just want to either accept our/their code, you can use flag `-X theirs` or `-X ours` with all git commands doing either merge/rebase.


| Currently on | Command | Strategy | Outcome |
| --- | --- | --- | --- |
| master | git merge feature | **\-Xtheirs** | Keep changes from feature branch |
| master | git merge feature | **\-Xours** | keep changes from master branch |
| feature | git rebase master | **\-Xtheirs** | Keep changes from feature branch |
| feature | git rebase master | **\-Xours** | keep changes from master branch |


### Show current head

```
git rev-parse HEAD
```
