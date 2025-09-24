---
title: Tcpdump
date: 2025-03-29 06:45:48Z
updated: 2025-09-24 11:52:04Z
taxonomies:
  tags:
  - linux
  - networking
---


- Check `man pcap-filter` for tcpdump expression syntax and fields
- Capture file
```
tcpdump -w capture.pcap -i any host google.com
```
