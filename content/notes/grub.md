---
title: Grub
date: 2025-04-08 08:08:22Z
updated: 2025-09-24 11:51:56Z
taxonomies:
  tags:
  - linux
---

#### Update kernel options via grub

- Edit file `/etc/default/grub` with necessary change
- Finally run `grub2-mkconfig -o /boot/grub2/grub.cfg` (on rhel, centos) or `update-grub` on debian, ubuntu
	- if it doesn't work try adding option `--update-bls-cmdline` to grub2-mkconfig
	- for efi the path could be different: ``
