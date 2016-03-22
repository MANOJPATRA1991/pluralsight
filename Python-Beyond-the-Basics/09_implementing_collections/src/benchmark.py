# -*- coding: utf-8 -*-

from random import randrange
from timeit import timeit

from sorted_set import SortedSet

S = SortedSet(randrange(1000) for _ in range(2000))


def main():
    elapsed_time = timeit(
        setup='from __main__ import S',
        stmt='[S.count(i) for i in range(1000)]',
        number=100
    )
    print(elapsed_time)

if __name__ == '__main__':
    main()
