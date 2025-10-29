# ft_package

This is a blueprint for the creation of a package in Python.

```bash
$>pip show -v ft_package
Name: ft_package
Version: 0.0.1
Summary: A sample test package
Home-page: https://github.com/bchene/ft_package
Author: bchene
Author-email: bchene@student.42angouleme.fr
License: MIT
Location: /home/bchene/...
Requires:
Required-by:
Metadata-Version: 2.1
Installer: pip
Classifiers:
Entry-points:
$>
```

## Installation
The package will be installed via pip using one of the following commands : _(both should work)_
```bash
pip install ./dist/ft_package-0.0.1.tar.gz
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```


## Utilisation
Your package must be able to be called from a script like this one:
```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto")) # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu")) # output: 0
```
