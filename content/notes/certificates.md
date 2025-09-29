---
title: Certificates
date: 2024-11-23 09:43:29Z
updated: 2025-09-29 17:31:16Z
taxonomies:
  tags:
  - security
---


### Create a new root CA, then create a new certificate and private key using step cli

```
$ step certificate create root-ca root-ca.crt root-ca.key --profile root-ca

$ step certificate create foo foo.crt foo.key --profile leaf \
            --ca root-ca.crt --ca-key root-ca.key --san 10.230.32.1 --san 10.230.32.2
```

### Openssl inspect certificate

```
$ openssl x509 -in input.crt -noout -text
```

### Remove passphrase from a private key

```
$ openssl ec -in input.key -out output.key
```

