#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys
import io


class TriangleError(Exception):

    def __init__(self, text, sides):
        super().__init__(text)
        self._sides = tuple(sides)  # prevent modification (read-only)

    @property
    def sides(self):
        return self._sides

    def __str__(self):
        return "'{}' for sides {}".format(self.args[0], self._sides)

    def __repr__(self):
        return "TriangleError({!r}), {!r}".format(self.args[0], self._sides)


def triangle_area(a, b, c):
    sides = sorted((a, b, c))
    if sides[2] > sides[0] + sides[1]:
        raise TriangleError("Illegal triangle", sides)
    p = (a + b + c) / 2
    a = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return a


def main():
    triangles = (
        (3, 4, 5),  # legitimate
        (3, 4, 10),
    )
    for tri in triangles:
        message = "triangle_area{}: \t ".format(tri)
        try:
            message += str(triangle_area(*tri))
        except TriangleError as e:
            try:
                print(e, file=sys.stdin)
            except io.UnsupportedOperation as f:
                print(e)
                print(f)
                print(f.__context__ is e)
        else:
            print(message, file=sys.stdout)

if __name__ == '__main__':
    main()
