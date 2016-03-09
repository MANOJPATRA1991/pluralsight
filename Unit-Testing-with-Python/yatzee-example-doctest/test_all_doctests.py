#!/usr/bin/env python
# -*- coding: utf-8 -*-

import doctest
import unittest
import yatzee


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(yatzee))
    return tests
