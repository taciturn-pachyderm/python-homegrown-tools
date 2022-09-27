---
title: Quickstart
---

<style>
  /* Add divider line between sections before the heading */
  h2 {
    border-top: 1px dotted var(--md-default-fg-color--lighter);
    padding-top: 1.25rem;
  }
</style>


## Init

```python
d = dotdict()
d.e = 4
d.f = "5"
d.g = True
d.h = { "a": 3, "b": "string", "c": False }
d.i = d.e

assert type(d.h) == dotdict
assert d.e == d.i == 4
assert d.f == "5"
assert d.g == True
```