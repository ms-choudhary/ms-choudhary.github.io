---
title: Golang
date: 2024-09-24 09:32:10Z
updated: 2025-05-06 07:32:03Z
taxonomies:
  tags:
  - golang
---

### CommandLine

- After parsing flags you can get other arguments via: `flag.Args()` (array) or `flag.Arg(i)` specific arg. `flag.Narg` = number of args

### Time

- [Layout string in time](https://pkg.go.dev/time@go1.23.2#Time.Format).Parse and time.Format expects this date (reference date): 01/02/2006  `Jan 2 15:04:05 2006 MST` (Note the date should be this specific date and time for it to parse successfully). Following shows some example:

```
time.Parse("01/02/2006", "10/02/2024")
time.Parse("02 of 01 2006", "02 of 10 2024")
```

### Sql

- For database sql, checkout [this wiki](https://go.dev/wiki/SQLInterface)

### Logging

- For serial logging, checkout [slog](https://pkg.go.dev/log/slog)

### Golang build

- To cross compile go binary for different os and arch run:

```
env GOOS=target-OS GOARCH=target-architecture go build package-import-path
```

where target-os can be: `linux, darwin, android, windows, freebsd, netbsd, openbsd, dragonfly, plan9`  
where target-architecture can be: `arm, arm64, amd64`

- Use `embed` package to add files to binary at compile time

### Local dependency

To use local version of the dependency, you can clone the deps in dir $DEP, then use replace directive in go mod

`$ go mod edit -replace github.com/google/go-cmp=$DEP`

### [Array, Slices](https://go.dev/blog/slices)

- Array is the building block of contingous items, contains size as part of it's definition. eg `var buffer [256]byte`. Arrays are always fixed size.
- Slice is a datastructure which describes a contiguous section of array: `var slice []byte = buffer[100:150]`. Behind the scenes, it contains the pointer to array, length and capacity (maximum length to which slice can extend).

### [String, Rune, Character, Byte](https://go.dev/blog/strings)

- String in golang is slice of bytes
- String literals are always utf-8 encoded. (Go source code) eg `const nihongo = "日本語"`
- In unicode standard, each character is represented by "code point" eg, U+2318 represents `⌘` , in golang this code point is referred as rune (aliased to int32)
- When you range through a loop, it decodes 1 utf-8 length rune on each loop

### Import local modules

Import other packages rather than main package

```
import (
  "noc-manager/pkg/models"
)
```

Run `go mod edit -replace noc-manager=../../noc-manager` to add a local dependency & run `go mod tidy`

Tip: Name modules as simple names rather than git urls unless you're planning on publishing them. Otherwise you might get weird issues.

### JSON or YAML omitempty or ignore

```
type T struct {
    F int `yaml:"a,omitempty"`
    B int `yaml:"-"` // this field will be ignored from rendering
}
```

```
type T struct {
    F int `json:"a,omitempty"`
    B int `json:"-"` // this field will be ignored from rendering
}
```
