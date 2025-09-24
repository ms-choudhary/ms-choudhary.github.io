---
title: Package Management
date: 2024-11-24 03:52:22Z
updated: 2025-09-24 05:21:44Z
taxonomies:
  tags:
  - linux
---

### Debian dpkg

```
# list inventory of packages and their version installed
$ dpkg -l

# List file contents of a package
$ dpkg -L tcpdump

# Reverse lookup, which package provides this file
$ dpkg-query -S /usr/bin/dig
```

Packaging systems can keep track of dependencies only if all softwares are installed via package management. If for eg, awscli was installed outside package management, dpkg won't know if upgrading python will break awscli. 

gpg keys are used to check the signature to validate if package was signed by trusted entity. 

### Fedora rpm

```
# list inventory
$ rpm -qa


# list content 
$ rpm -ql tcpdump

# verify integrity of a package; if it was modified
$ sudo rpm -V sudo
$ sudo rpm -Va  # all packages
```

### Netbsd vulnerability for packages

```
$ pkg_admin -V -v fetch-pkg-vulnerabilities
$ pkg_admin audit
```
