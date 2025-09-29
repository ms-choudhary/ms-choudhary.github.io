---
title: Files/Storage
date: 2024-11-23 09:47:48Z
updated: 2025-09-28 11:58:28Z
taxonomies:
  tags:
  - linux
---

### Useful commands
- Use `tac` or `tail -r` to reverse a file
- `cat -n filename` show file with linenumber
- `less -N filename or type -N in less window` show line numbers with less

### Copy via dd

```
if 'if=' not present it reads from stdin
if 'of=' not present it writes to stdout

bs = block size, default 512 bytes, change to 1 byte if you want to write single byte
count = no. of block size bytes to write for eg if bs=1, count=4 will write 4 bytes
seek = write at seek position to block size * number 

skip = skip block size * number while reading

printf '🐱' | dd of=/dev/xvd1 
dd if=/dev/xvd1 count=1 2> /dev/null | hexdump -C

printf "$(dd if=/dev/xvd1 bs=1 count=4 2> /dev/null)\n"

printf '🐱' | dd of=/dev/xvd1 bs=1 seek=4

printf "$(dd if=/dev/xvd1 bs=1 count=8 2> /dev/null)\n"
```
