#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def median(iterable):
    """Obtain the central value of a series.

    Sorts the iterable and returns the middle value if there is an even
    number of elements, or the arithmetic mean of the middle two elements
    if there is an even number of elements.

    Args:
        iterable: A series of orderable items.

    Returns:
        the median value.
    """
    items = sorted(iterable)
    if len(items) == 0:
        raise ValueError("median() arg is an empty sequence")
    median_index = (len(items) - 1) // 2
    if len(items) % 2 != 0:
        return items[median_index]
    return (items[median_index] + items[median_index + 1]) / 2.0


def main():
    iterables = (
        [5, 2, 1, 4, 3],
        [5, 2, 1, 4, 3, 6],
        [],
    )
    for i in iterables:
        try:
            print("{} \t {}".format(repr(i), median(i)))
        except ValueError as e:
            print("Payload: {}".format(e.args))
            print(str(e))

if __name__ == '__main__':
    main()
