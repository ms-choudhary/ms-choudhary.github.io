---
title: Terminal/Shell
date: 2024-09-24 09:47:30Z
updated: 2025-04-03 06:53:23Z
taxonomies:
  tags:
  - linux
---

### Keyboard Shortcuts

`CTRL-A` = go to the begining of the line  
`CTRL-E` = go to the end of the line  
`CTRL-U` = delete everything till begining  
`CTRL-K` = delete everyting till end

### Job control
- disown - removes the job from list of running jobs, so it doesn't get killed when you exit the terminal

### Terminal

Terminal is a pair master and slave devices. Slave devices are like dumb clients without any intelligence just relaying what user types to the server and showing back the response. 

Now when you type text on the terminal, it's relayed back to master device, which gives the information to program running. There're escape sequences to display text in bold or color, cursor movement etc. When you type `Ctrl-C` or `Ctrl-Z` it sends a ascii signal `\x03` and `26`. This is intercepted by kernel (and not userspace program like shell), and it sends `SIGINT` signal to process group in the terminal. 

When the master device starts, it makes this sys call:

```
syscall.Syscall(
    syscall.SYS_IOCTL,
    tty.Fd(),
    syscall.TIOCSWINSZ,
    uintptr(unsafe.Pointer(&resizeMessage)),
)
```

this calls the ioctl system call. To check terminal parameters, you can type:

```
stty -a

or

tputs cols # for columns 
```

when you change the window size of the terminal, kernel sends a signal `SIGWINCH` which resets the stty cols etc. The side effect of this not being correctly set will result in overwriting of text of same line and not changing to next line on inputting long text in the terminal. 

### Line numbers with less

```
less -N filename
or type -N in less window
```
