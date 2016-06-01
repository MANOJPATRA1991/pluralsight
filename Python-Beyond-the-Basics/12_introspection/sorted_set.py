#!/usr/bin/python3
# -*- coding: utf-8 -*-

from bisect import bisect_left
from collections.abc import Sequence, Set
from itertools import chain


class SortedSet(Sequence, Set):

    def __init__(self, items=None):
        self._items = sorted(set(items)) if items is not None else []

    def __contains__(self, item):
        # ALTERNATIVE =>
        try:
            self.index(item)
            return True
        except ValueError:
            return False

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        for item in self._items:
            yield item

    def __getitem__(self, index):
        result = self._items[index]
        return SortedSet(result) if isinstance(index, slice) else result

    def __repr__(self):
        return "SortedSet({})".format(
            repr(self._items) if self._items else ''
        )

    def __eq__(self, rhs):
        # it's important to return NotImplemented
        # rather than raise NotImplementedError
        if not isinstance(rhs, SortedSet):
            return NotImplemented
        return self._items == rhs._items

    def __ne__(self, rhs):
        if not isinstance(rhs, SortedSet):
            return NotImplemented
        return self._items != rhs._items

    def _is_unique_and_sorted(self):
        return all(self[i] < self[i + 1] for i in range(len(self) - 1))

    def index(self, item):
        """Implemented with binary search.

        As such, assumes that the elements of the class are sorted.
        """
        assert self._is_unique_and_sorted()
        index = bisect_left(self._items, item)
        if (index != len(self._items)) and (self._items[index] == item):
            return index
        raise ValueError("{} not found".format(repr(item)))

    def count(self, item):
        """Peforms simple membership test.

        As such, depends on there being not duplicates.
        """
        assert self._is_unique_and_sorted()
        return int(item in self)

    def __add__(self, rhs):
        return SortedSet(chain(self._items, rhs._items))

    def __mul__(self, rhs):
        return self if rhs > 0 else SortedSet()

    def __rmul__(self, lhs):
        return self * lhs

    def issubset(self, iterable):
        return self <= SortedSet(iterable)

    def issuperset(self, iterable):
        return self >= SortedSet(iterable)

    def intersection(self, iterable):
        return self & SortedSet(iterable)

    def union(self, iterable):
        return self | SortedSet(iterable)

    def symmetric_difference(self, iterable):
        return self ^ SortedSet(iterable)

    def difference(self, iterable):
        return self - SortedSet(iterable)
