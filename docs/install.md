---
hide:
  - toc
---

```{.console, .prompt }
pip install -i https://pypi.example.com/simple/ example-policy-templates
```

```{.console, .prompt }
pip install --extra-index-url https://pypi.example.com/simple/ example-policy-templates boto3
```


```console title="requirements.txt" hl_lines="1"
--extra-index-url https://pypi.example.com/simple/
example-policy-templates>=0.0.1
boto3

```

```{.console, .prompt }
pip install example-policy-templates
```