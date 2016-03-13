`str()` and `repr()` are Functions for making **string representations** from Python objects which call the methods `__str()__` and `__repr()__`

# `repr()`

The **built-in** function produces an **unambiguous** string representation of an object. It sshould include type of the object along with other identifying fields

`Point2D(x=42, y=69)`

- Exactness is more important than human-friendliness
- Suited for debugging
- Includes identifying information
- Generally best for logging

The result of `repr()` should generally contain **more information** than the result of `str()`

`repr()` is for developers, where `str()` is for clients.

As a rule, you should **always write** a `repr()` for your classes. The default `repr()` is not very helpful.

- written: `Point2D(x=3, y=5)`
- default: `<point.Point2D object at 0x103a7e950>`

`repr()` is used when showing elements of a collection.


# `str()`

The **built-in** function produces a **readable**, human-friendly representation of an object. Generally not program oriented.

Remember - `str()` is also the string constructor.

By default, `str()` simply calls `repr()`. However, `repr()` does NOT call `str()`.

# `__format__()`

The **special** method invoked by `str.format()`

Replacement fields: `{field_name: format_spec}`. Optional **format specification** after colon.

Be default, `__format__()` just calls `__str__()`.

You can use force format to use `repr()` by placing `!r` in the formatting placeholder: `{!r}'.format(Point2D(1, 2))`

Similarly, you can use explicity use `str()` representation by placin `!s`: `{!s}.format(Point2D(1, 2))`

Sometimes, the `repr()` of an object will be shorter than its `str()`.

# `reprlib`

The **standard library** module that supports alternative implementations of `repr()`

- limits otherwise excessive string length
- useful for large collections

## `reprlib.repr()`

The **standard library** function is a **drop-in replacement** for `repr()`

## `reprlib.Repr`

The **standard library** class

- implements the main functionality of `reprlib`
- supports customization through *subclassing*
- <http://docs.python.org/3/library/reprlib.html>

`reprlib.aRepr`: an **instance** used by Python and debuggers


# Other Built-in Functions

## `ascii()`

The **built-in** function replaces non-ASCII characters with escape sequences

Useful in situations where:

- you need to serialize data as ASCII 
- you can't communicate encoding information but don't want to lose unicode data

## `ord()`

The **built-in** function converts a single character to its **integer** Unicode *codepoint*. 

## `chr()`

The **built-in** function converts an **integer** Unicode *codepoint* to a single character string.

Given `x` and `y`, `chr(ord(x)) == x` and `ord(chr(y)) == y`


# Summary

- Python has two primary string representation methods: `str(obj)` and `repr(obj)`
- `__repr__(self)` should produce an unambigious, precise representation of an object, which should include type and any other identifying information. For developers.
- You should always implement `__repr__()` for your classes
- Default `__repr__()` is not very useful
- `__str__(self)` is for human consumption; doesn't need to be too precise. Has fallback to `repr()`
- `"{:f}".format(obj)` calls `__format__(self, f)`. Falls back to `str()`
- `reprlib` provides a **drop-in replacement** for `repr()` which limits output size
- `reprlib` is useful for printing large data structures
- `reprlib` implements the class `Repr`
- `reprlib.Repr` is designed to be extended and customized via inheritance
- `ascii(string)` replaces non-ASCII characters in a Unicode string with escape sequeunces
- `ord()` takes a single character Unicode string and converts it to a Unicode codepoint
- `chr()` reverse the `ord()` (inverses of one another)
- Good `__repr__` functions are easy to write and can improve debugging and reporting errors
