# Protocols

- To implement a protocol, objects must support certain operations
- Most collections implement *container*, *sized*, and *iterable*
- All except `dict` and `set` are *sequences*
- Types
    - **Container**: membership testing using `in` and `not in`
    - **Sized**: number of elements with `len(s)`
    - **Iterable**: can produce an *iterator* with `iter(s)`
    - **Sequence**:
        - Retrieve elements by index: `item = seq[index]`
        - Find items by value: `index = seq.index(item)`
        - Count items: `num = seq.count(item)`
        - Produce a reversed sequence: `r = reversed(seq)`
    - **Set**:
        - subset, proper subset
        - equal, not equal
        - proper superset, superset
        - intersections
        - union
        - symmetric difference

---


# `SortedSet`

A collection with is **sized, iterable, sequence container** of a **set** of distinct items and constructible from an iterable


## `Container` protocol

- Membership testing using `in` and `not in`
- Special method: `__contains__(item)`
- Fallback to **iterable** protocol

## `Sized` protocol

- Number of items using `len(sized)` function
- Must **not** consume or modify collection

## `Iterable` protocol

- Obtain iterator with `iter(iterable)` function
- Special method: `__iter__()`

## `Sequence` protocol

- Retrieves slices by slicing: `item = seq[index]`
- Retrieves slices by slicing: `item = seq[start:stop]`
- Produce a reversed sequence: `r = reversed(seq)` (fallback to `__getitem__()` and `__len__()`)
- Find items by value: `index = seq.index(item)`
- Count items: `num = seq.count(item)`
- Concatenation with a `+` operator (special method `__add__()`)
- Repetition with `*` operator (special methods `__mul()__` and `__rmul__()`)

## Equality and Inequality

- Equality:
    - `lhs == rhs`
    - Special method: `__eq__(self, rhs)`
    - `self` argument is `lhs` left-hand-side operand
- Inequality
    - `lhs != rhs`
    - special method: `__ne__(self, rhs)`
    - `self` argument is `lhs` left-hand-side operand

# `Set` protocol

- `__le__()`
- `__lt__()`
- `__eq__()`
- `__ne__()`
- `__gt__()`
- `__ge__()`
- `__and__()`
- `__or__()`
- `__xor__()`
- `__sub__()`
- `isdisjoint()`
