---
title: Initrd
date: 2025-09-12 10:45:50Z
updated: 2025-09-24 11:58:09Z
taxonomies:
  tags:
  - linux
---

## Extract

```
xzcat initrd.img | cpio -id

-i extract
-d create dirs
```

## Check content

```
# show content of initramfs of current kernel
lsinitrd

# show content of specific initramfs file
lsinitrd path/to/initramfs.img
```
