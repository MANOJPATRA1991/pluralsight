# Definitions

`def`: define new functions, executed at runtime

# LEGB Rule

1. Local
2. Enclosing
3. Global
4. Built-in

```python
PI = TAU / 2

def func(x):
    def local_func(n):
        a = 'hello, '
        return a + n

    y = 2
    return x + y
```

```
>>> g = 'global'
>>> def outer(p='param'):
...     l = 'local'
...     def inner():
...             print(g, p, l)
...     inner()
... 
>>> outer()
global param local
>>> outer.inner()
    ...
AttributeError: 'function' object has no attribute 'inner'
```

LEGB does **not apply** when making **new bindings**.

# Local functions

- Useful for specialized, one-off functions
- Aid in code organization and readability
- Similar to lambdas, but more general
    - May contain multiple expressions
    - May contain statements


# Returning functions

```
>>> def enclosing():
...     def local_func():
...             print('local func')
...     return local_func
... 
>>> lf = enclosing()
>>> lf()
local func
```

**First-class functions**: functions can be treated like any other object.


# Closures

Maintains references to objects from earlier scopes.

The local function closes over the objects it needs, preventing them from being *garbage-collected*.

```
>>> def enclosing():
...     x = 'closed over'
...     def local_func():
...             print(x)
...     return local_func
... 
>>> lf = enclosing()
>>> lf()
closed over
>>> lf.__closure__
(<cell at 0x7fc662326948: str object at 0x7fc65dea8cb0>,)
```

# Function factory

Function that returns new, specialized functions.

```
>>> from raise_to import raise_to
>>> square = raise_to(2)
>>> square.__closure__
(<cell at 0x7f16ac46f948: int object at 0x9f4280>,)
>>> square(5)
25
>>> square(9)
81
>>> square(1234)
1522756
>>>
>>> cube = raise_to(3)
>>> cube(3)
27
>>> cube(10)
1000
```


# Scope Demos

```python
def enclosing():
    message = 'enclosing'

    def local():
        message = 'local'

    print('enclosing message:', message)
    local()
    print('enclosing message:', message)

print('global message:', message)
enclosing()
print('global message:', message)
```

Output:

```
global message: global
enclosing message: enclosing
enclosing message: enclosing
global message: global
```

## `global`:

Introduces names from global namespace into the local namespace

```python
def enclosing():
    message = 'enclosing'

    def local():
        global message
        message = 'local'

    print('enclosing message:', message)
    local()
    print('enclosing message:', message)

print('global message:', message)
enclosing()
print('global message:', message)
```

Output:

```
global message: global
enclosing message: enclosing
enclosing message: enclosing
global message: local
```

## `nonlocal`

- introduce names from the enclosing namespace into the local namespace
- you get a `SyntaxError` if the name doesn't exist

```python
def enclosing():
    message = 'enclosing'

    def local():
        nonlocal message
        message = 'local'

    print('enclosing message:', message)
    local()
    print('enclosing message:', message)

print('global message:', message)
enclosing()
print('global message:', message)
```

Output:

```
global message: global
enclosing message: enclosing
enclosing message: local
global message: global
```


# Decorators

We've seen **functions as decorators**... but **other objects** can be decorators **as well**.

Remember, classes can be called, so classes can de decorated. However, this means that if one were to use a decorator for a class, `__call__` must be implemented so the instance can be called.

## Instances as decorators

`tracer.py`: 

```python
class Trace:

    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print('Calling {}'.format(f))
            return f(*args, **kwargs)
        return wrap

tracer = Trace()

@tracer
def rotate_list(l):
    return l[1:] + [l[0]]
```

REPL Output:

```
>>> from tracer import rotate_list, tracer
>>> l = [1, 2, 3]
>>> l = rotate_list(l)
Calling <function rotate_list at 0x7f42b4b33620> 
>>> l
[2, 3, 1]
>>> l = rotate_list(l)
Calling <function rotate_list at 0x7f42b4b33620>
>>> l
[3, 1, 2]
>>> 
>>> tracer.enabled = False
>>> l = rotate_list(l)
>>> l
[1, 2, 3]
```

## Multiple decorators

```python
@decorator1
@decorator2
@decorator3
def some_function():
    ...
```


# `functools.wrap()`

**Naive decorators** can lose important metadata.

For example:

```python
import functools

def noop(f):
    def noop_wrapper():
        return f()
    return noop_wrapper

@noop
def hello():
    """Print a well-known message."""
    print("Hello, world!")
```

Output:

```
>>> from noop import hello
>>> hello.__name__
'noop_wrapper'
>>> hello.__doc__
```

To fix this problem, edit the decorator with `functools.wrap()`:

```python
import functools

def noop(f):
    @functools.wraps(f)
    def noop_wrapper():
        return f()
    return noop_wrapper

@noop
def hello():
    """Print a well-known message."""
    print("Hello, world!")
```

Output:

```
>>> from noop import hello
>>> hello.__name__
'hello'
>>> hello.__doc__
'Print a well-known message.'
```


===


# Summary

- `def` is executed at run-time
- `def` defines the function in a scope from which it's called
- functions defined inside other functions are called **local functions**
- a new local function is created each time a containing function is executed
- local functions are no different from other local name-bindings and can be treated like any other object
- local functions can access names and other scopes via the **LEGB rule**
- the enclosing scope for local functions includes the paramteres of its enclosing function
- local functions can be useful for code organization
- local functions are similar to lambdas but are more general and powerful
- functions can return other functions, including local functions defined in their bodies
- closures allow local functions to access objects from scopes which have terminated
- closures ensure that objects from terminated scopes are not garbage collected
- functions with closures have a special `__closure__` attribute
- local functions in closures are the keys im implementing **function factories**, which are functions that create other functions
- function decorators are used to modify the behavior of existing functions without having to change them directly
- decorators are callable objects which accept a single callable object as an argument and return a new callable object
- you use the `@` symbol to apply a decorator to functions
- decorators can enhance maintainability, readability, and scalability of the designs
- decorators can be any kind of callable object (functions, class objects, class instance)
- the `__name__` and `__doc__` attributes of decorated functions are actually those of their replacement function which is not always what you want
- you can manually update the `__name__` and `__doc__` of the wrapper function
- you can achieve the same by using the wrapper function `@functools.wraps`
- multiple decorators can be applied to a function
- when there are multiple decorators, they are applied in reverse order
- decorators don't have to be specially designed to work with other decorators
- decorators are a powerful tool, but make sure you don't overuse them or use them unnecessarily
- there is technically no decorators that take extra arguments
- to paramterize decorators, you need a function that creates decorators
- local functions can create closures over objects on any number of enclosing scopes
