# -*- coding: utf-8 -*-
"""
Generate random values for iteration streaming.
Demo-only with a fake Sensor class.
"""

import datetime
import itertools
import random
import time


class Sensor:

    def __iter__(self):
        return self

    def __next__(self):
        return random.random()


def main():
    sensor = Sensor()
    timestamps = iter(datetime.datetime.now, None)

    for stamp, value in itertools.islice(zip(timestamps, sensor), 10):
        print(stamp, value)
        time.sleep(1)

if __name__ == '__main__':
    main()
