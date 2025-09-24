---
title: IDrac/Racadm
date: 2024-11-17 06:30:42Z
updated: 2025-09-24 11:52:21Z
taxonomies:
  tags:
  - linux
---


iDRAC is a separate BMC chip which integrates on the motherboard, and provides users to control a server remotely. You could build a similar feature with piKVM, [diy](https://docs.pikvm.org/v2/):
- Connect the video cable.
- Integrate circuit to motherboard power supply

With serial over lan, you can get serial console remotely for troubleshooting purposes. 

### Alias

```
alias myracadm="racadm -r 10.118.16.5 -u root -p calvin --nocertwarn"
```

### Check sel logs

```
/opt/index/ops-bin/rracadm.sh pro-XX-Y.dcaux.indexww.com getsel -o
```


### Check cpu reset

```
/opt/index/ops-bin/rracadm.sh db-maria-bh2ingest-3 lclog view -n 10 -k CPU
```

### Set first boot to pxe

```
racadm -r 10.118.16.3 -u root -p calvin set idrac.serverboot.firstbootdevice PXE
```

### pxe device

```
./racadm get BIOS.PxeDev1Settings.PxeDev1Interface

./racadm set BIOS.PxeDev1Settings.PxeDev1Interface <interface name, something like NIC.Slot.1-1>
```

### Powercycle

```
racadm -r 10.118.16.3 -u root -p calvin serveraction powercycle
```

### Jobqueue

```
myracadm jobqueue create BIOS.Setup.1-1 -r pwrcycle
```

### racreset

```
racadm racreset soft
```

### Via ssh

```
ssh root@idrac_ip
ssh -o KexAlgorithms=curve25519-sha256 root@idrac_ip
console com2
```

ctrl + \ to exit


### System info

```
racadm getsysinfo
```
