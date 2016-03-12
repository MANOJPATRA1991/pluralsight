#!/usr/bin/env python
# -*- coding: utf-8 -*-


def raise_to(exp):
    def raise_to_exp(x):
        return pow(x, exp)
    return raise_to_exp


