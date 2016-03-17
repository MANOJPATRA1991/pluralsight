# Comprehensions

Short-hand syntax for creating collections and iterable objects

```
>>> d = {i : i * 2 for i in range(10)}
>>> type(d)
<type 'dict'>
>>> s = {i for i in range(10)}
>>> type(s)
<type 'set'>
>>> g = (i for i in range(10))
>>> type(g)
<type 'generator'>
```

```
>>> points = []
>>> for x in range(5):
...     for y in range(3):
...             points.append((x,y))
... 
>>> points
[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2)]
```

## Benefits of comprehensions

- Container populated "atomically"
- Allows Python to optimize creation
- More readable


## Nested Comprehensions

See `nested_comprehensions.py`


---


# Iteration and Iterables + Building-Block Functions

*Functional*-style Python


## `map()`

Apply a function to every element in a sequence, producing a new sequence

```python
>>> from tracer import Trace
>>> result = map(Trace()(ord), 'The quick brown fox')
>>> result
<map object at 0x7f17646ecc88>
>>> next(result)
Calling <built-in function ord>
84
>>> next(result)
Calling <built-in function ord>
104
>>> next(result)
Calling <built-in function ord>
101
>>> list(map(ord, 'The quick brown fox'))
[84, 104, 101, 32, 113, 117, 105, 99, 107, 32, 98, 114, 111, 119, 110, 32, 102, 111, 120]
>>> for o  in map(ord, 'The quick brown fox'):
...     print(o)
... 
84
104
101
32
113
117
105
99
107
32
98
114
111
119
110
32
102
111
120
```

`map()` ...

- is **lazy** - it only produces values as they're **needed**.
- can accept **any number** of input sequences

The number of input sequences must **match** the number of function arguments

```
>>> sizes = ['small', 'medium', 'large']
>>> colors = ['lavender', 'teal', 'burnt orange']
>>> animals = ['koala', 'platypus', 'salamander']
>>> def combine(size, color, animal):
...     return '{} {} {}'.format(size, color, animal)
... 
>>> list(map(combine, sizes, colors, animals))
['small lavender koala', 'medium teal platypus', 'large burnt orange salamander']
>>> 
>>> import itertools
>>> def combine(quantity, size, color, animal):
...     return '{} x {} {} {}'.format(quantity, size, color, animal)
... 
>>> list(map(combine, itertools.count(), sizes, colors, animals))
['0 x small lavender koala', '1 x medium teal platypus', '2 x large burnt orange salamander']
```


# `filter()`

Passing `None` as the **first argument** to `filter()` will remove elements which evaluate to `False`.


# `functools.reduce()`

Repeatedly apply a function to the elements of a sequence, reducing them to a single value

Equal to...

- `fold` in functional programming
- `aggregate` in LINQ
- `std:accumulate()` in C++ STL

Optional **initial value** is conceptually just **added** to the start of the input sequence.

```
>>> from functools import reduce
>>> import operator
>>> reduce(operator.add, [1,2,3,4,5])
15
>>> numbers = [1,2,3,4,5]
>>> accumulator = operator.add(numbers[0], numbers[1])
>>> for item in numbers[2:]:
...     accumulator = operator.add(accumulator, item)
... 
>>> accumulator
15
>>> def mul(x, y):
...     print('{} * {}'.format(x, y))
...     return x * y
... 
>>> reduce(mul, range(1,10))
1 * 2
2 * 3
6 * 4
24 * 5
120 * 6
720 * 7
5040 * 8
40320 * 9
362880
>>> reduce(mul, [])  # error with empty list
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: reduce() of empty sequence with no initial value
>>> reduce(mul, [1])  # never called
1
```


# map-reduce

See `map_reduce.py`


---


# `iterable`

An object which implements the `__iter__()` method


# `iterator`

An object which implements the *iterable protocol* and which implements the `__next__()` method

The **alternative** iterable protocol works with any object that supports consecutive **integer indexing** via the `__getitem__()`


# Extended `iter()`

`iter(callable, sentinel)`

Callable object takes zero arguments; iteration stops when `callable` produces value equal to `sentinel`

Extended `iter()` is often used for creating **infinite sequences** from existing functions

```
>>> import datetime
>>> i = iter(datetime.datetime.now, None)
>>> next(i)
datetime.datetime(2016, 3, 9, 11, 1, 49, 402807)
>>> next(i)
datetime.datetime(2016, 3, 9, 11, 1, 49, 402908)
>>> next(i)
datetime.datetime(2016, 3, 9, 11, 1, 49, 994614)
```

# Real World Iterables - Sensor Data

See `.py`
