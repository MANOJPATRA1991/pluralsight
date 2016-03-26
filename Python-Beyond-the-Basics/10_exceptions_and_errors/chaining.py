#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import traceback


class InclinationError(Exception):
    pass


def inclination(dx, dy):
    try:
        return math.degrees(math.atan(dy / dx))
    except ZeroDivisionError as e:
        raise InclinationError("Slope cannot be vertical") from e


def main():
    points = (
        (0, 5),
    )
    for p in points:
        try:
            inclination(*p)
        except InclinationError as e:
            print(e)
            print(e.__cause__)
            print(e.__traceback__)
            traceback.print_tb(e.__traceback__)
            # s = traceback.format_tb(e.__traceback__)
            # print(s)

if __name__ == '__main__':
    main()
    print("Finished")  # program will still finish, trust me
