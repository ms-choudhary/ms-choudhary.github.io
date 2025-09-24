---
title: Terraform
date: 2024-09-24 09:48:21Z
updated: 2025-09-24 11:52:38Z
taxonomies:
  tags:
  - tooling
---

### For each and count meta argument

Ideally each block maps to one infrastructure component. There're two ways to create map multipe by just one block. 

`count` 

```
resource "aws_instance" "server" {
  count = 4 # create four similar EC2 instances

  ami           = "ami-a1b2c3d4"
  instance_type = "t2.micro"

  tags = {
    Name = "Server ${count.index}"
  }
}
```

`for_each` - accepts a map, list or set

```
resource "azurerm_resource_group" "rg" {
  for_each = tomap({
    a_group       = "eastus"
    another_group = "westus2"
  })
  name     = each.key
  location = each.value
}
```
