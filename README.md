## About 
Command Line Application and Python Package to Add/Append/Remove environment variables on Windows systems  
Current package allows to precisely control and differentiate user and system variables 

## Table of Contents
1. [Installation](#installation)
2. [CLI](#how-to-use-as-cli-application)
    1. [Get variable](#get-variable-cli)
    2. [Create/Replace variable](#createreplace-variable-cli)
    3. [Append to existing variable](#append-to-existing-variable-cli)
    4. [Delete variable](#delete-variable-cli)
    5. [List all variables](#list-all-variables-cli)
3. [Python Package](#how-to-use-as-python-package)
    1. [Get variable](#get-variable)
    2. [Create/Replace variable](#createreplace-variable)
    3. [Append to existing variable](#append-to-existing-variable)
    4. [Delete variable](#delete-variable)
    4. [List all variables](#list-all-variables)


## Installation
To install the package you need to run
```
python -m pip install py-setenv
```

## How to use as CLI application
### Get variable (CLI)
Get value of variable _my_var_ 
```batch
:: User environment
setenv my_var -u
:: System environment
setenv my_var
```

### Create/replace variable (CLI)
Set variable _my_var_ to _1_  
```batch
:: User environment
setenv my_var -v 1 -u

:: System environment
setenv my_var -v 1
```

### Append to existing variable (CLI)
Append _my/test/dir_ to _path_ variable
```batch
:: User environment
setenv path -v my/test/dir -a -u

:: System environment
setenv path -v my/test/dir -a 
```

### Delete variable (CLI)
Delete variable _my_var_
```batch
:: User environment
setenv my_var -d -u

:: System environment
setenv my_var -d
```

### List all variables (CLI)
Lists all variables
```batch
:: User environment
setenv -l

:: System environment
setenv -l
```

## How to use as Python package

### Get variable

Get value of variable _my_var_

```python
from py_setenv import setenv
setenv("my_var")
```

Note Throws error KeyError when Enviroment variable is not found

### Create/replace variable
Set variable _my_var_ to _1_  
```python
from py_setenv import setenv
setenv("my_var", value=1, user=True)
```

### Append to existing variable
Append _my/test/dir_ to _path_ variable
```python
from py_setenv import setenv
setenv("path", value="my/test/dir", append=True, user=True)
```

### Delete variable
Delete variable _my_var_
```python
from py_setenv import setenv
setenv("my_var", delete=True, user=True)
```

### List all variables
Lists all variables
```python
from py_setenv import setenv
setenv(list_all=True)

# to suppress echo to console
setenv(list_all=True, suppress_echo=True)
```