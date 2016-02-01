#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_prefix(s1, s2):
    if (len(s1) > len(s2) or
            s1 not in s2):
        return False
    else:
        return s1 == s2[:len(s1)]


def is_extension(s1, s2):
    if (len(s2) > len(s1) or
            s2 not in s1):
        return False
    else:
        return s2 == s1[:len(s2)]


class Phonebook:

    def __init__(self):
        self.entries = {}

    def add(self, name, number):
        self.entries[name] = number

    def lookup(self, name):
        return self.entries[name]

    def get_names(self):
        return self.entries.keys()

    def get_numbers(self):
        return self.entries.values()

    def is_consistent(self):
        number_entries = self.get_numbers()
        for i in xrange(len(number_entries) - 1):
            for j in xrange(i + 1, len(number_entries)):
                n1 = number_entries[i]
                n2 = number_entries[j]
                if is_prefix(n1, n2) or is_extension(n1, n2):
                    return False
        return True
