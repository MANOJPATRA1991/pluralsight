# -*- coding: utf-8 -*-

values_lc = [x / (x - y)
             for x in range(100)
             if x > 50
             for y in range(100)
             if x - y != 0]

values_fl = []
for x in range(100):
    if x > 50:
        for y in range(100):
            if x - y != 0:
                values_fl.append(x / (x - y))

assert values_fl == values_lc


result_lc = [(x,y) for x in range(10) for y in range(x)]

result_fl = []
for x in range(10):
    for y in range(x):
        result_fl.append((x,y))
