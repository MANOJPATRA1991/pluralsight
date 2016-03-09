# Modules and Packages

A module which can contain other modules

Packages are generally directories, and modules are generally files

```python
>>> import urllib
>>> import urllib.request
>>> type(urllib)
<class 'module'>
>>> type(urllib.request)
<class 'module'>
>>> urllib.__path__
['/usr/lib/python3.4/urllib']
>>> urllib.request.__path__
    ...
AttributeError: 'module' object has no attribute '__path__'
```

## How Does Python Locate Modules?

`sys.path`: list of directoreis Python searches for modules

`PYTHONPATH`:

- Environment variable listing paths added to `sys.path`
- Uses the same format as your system `PATH` variable

## Basic Package Structure

```
path_entry/             # must be in sys.path
    my_package/         # package root
        __init__.py     # package init file
```

## Review

1. Package are modules that contain other modules.
2. Packages are generally implemented as directories containing a special `__init__.py` file
3. The `__init__.py` file is executed when the package is imported.
4. Packages can contain sub packages which themselves are implemented with `__init__.py` files in directories.


# Imports

## Absolute

- imports which use a full path to the module
- `from reader.reader import reader`

## Relative Imports

- imports which use a relative path to modules **in the same package**
- one dot = same directory; two dots = parent directory

### Summary

1. Can reduce typing in deeply nested package structures
2. Promote certain forms of modifiability
3. Can aid package renaming and refactoring
4. General advice is to avoid them in most cases

## Example

```
farm/
    __init__.py
    bird/
        __init__.py
        chicken.py
        turkey.py
    bovine/
        __init__.py
        cow.py
        ox.py
        common.py
```

absolute: `from farm.bovine.common import ruminate`

relative:

- `from .common import ruminate`
- `from . import common` (but requires use of `common.ruminate()`)


# `__all__`:

- list of attribute names import via `from module import *`
- must be a list of strings


# namespace packages

- packages split across several directories
- useful for splitting large packages into multiple parts
- defined in [PEP420](http://www.python.org/dev/peps/pep-0420)
- have no **`__init__.py` file**
- this avoids **complex initializiation** ordering **problems**.

## Import namespace packages

1. Python scans all entries in `sys.path`
2. If a matching directory with `__init__.py` is found, a normal package is loaded
3. If `foo.py` is found, then it is loaded
4. Otherwise, all matching directories in `sys.path` are considered part of the namespace package


# Executable Directories

Directories containing an entry point for Python execution

If `path1` directory has nothing:

```
$ python3 path1
... : can't find '__main__' module in 'path1'
```

Put a `__main__.py` file in the parent directory to make it executable

```
$ python3 path1
executing __main__.py with name __main__
```

### Executable Zip File

Zip file containing an entry point for Python execution

## Recommended Project Structure

```
project_name/ 
    __main__.py
    project_name/
        __init__.py
        more_source.py
        subpackage1/
            __init__.py
        test/
            __init__.py
            test_code.py
    setup.py
```


# Modules as Singletons

Modules are only executed once, when first imported - guarantees that initialization occurs only once

`registry.py`:

```python
_registry = []

def register(name):
    _registry.append(name)

def registered_names():
    return iter(_registry)
```

`use_registry.py`:

```python
import registry

registry.register('my name')

for name in registry.registered_names():
    print(name):
```


# Organizing Larger Programs Summary

- Packages are a special type of modules.
- Unlike modules, packages can contain other modules including other packages
- Package hierarchy is a powerful way to organize related code
- Packages have a `__path__` method which is a sequence specifying the directories from which a package is loaded
- `sys.path` is a list of directories where Python searches for modules
- `sys.path` is a normal list and can be modified and queried like any other list
- If you start Python with no arguments, an empty string is put at the front of `sys.path` - this instructs Python to import a module from the current directory
- Appending directories to `sys.path` at runtime allows modules to be imported from those directories
- `PYTHONPATH` is an environment variable containing a list of directories
- The format of `PYTHONPATH` is the same as system `PATH` variable
- Contents of `PYTHONPATH` is appended to the end of `sys.path`
- Normal packages are implemented by putting a file named `__init__.py` into a directoriy
- The `__init__.py` file in a directory is executed when the package is imported
- The `__init__.py` file can hoist attributes from sub-modules or higher namespaces for convenience
- Modules can be executed by python with the `-m` argument 
- Relative imports allow you to import modules within a package without specifying the full module path
- Relative imports must use the `from <module> import <name>` form of import
- Avoid relative imports because they can make the code harder to understand
- The `__all__` attribute of a module is a list of strings specifying the names to export when `from <module> import *` is used
- A namespace package is a package split across several directories 
- Namespace packages are described in PEP420
- Namespace packages don't use `__init__.py` files
- Namespace packages are created when one or more directories in the `PYTHONPATH` match an import request and no normal packages or modules match the request
- Each directory that contributes to a namespace package is listed in the packages in the `__path__` attribute
- Executable directories are executed by putting a `__main__.py` file in a directory
- If `__main__.py` is executed, the `__main__` attribute is set to `__main__`, and its parent directories are automatically added to `sys.path`
- Executable directories can be compressed into **.zip** files, which can be executed as well
- Executable directories and zip files are convenient ways to distribute Python programs 
- A simple standard project structure includes a location for non-Python files, a project package, and dedicated test subpackage
- Module level attributes provide a good mechanism for implementing singletons
- Modules have well defined initialization semantics
