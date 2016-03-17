# -*- coding: utf-8 -*-

values_lc = [[y * 3 for y in range(x)] for x in range(10)]

outer = []
for x in range(10):
    inner = []
    for y in range(x):
        inner.append(y * 3)
    outer.append(inner)

assert outer == values_lc

print(outer)

