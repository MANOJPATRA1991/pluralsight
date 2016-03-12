#!/usr/bin/env python
# -*- coding: utf-8 -*-


def escape_unicode(f):
    """
    Converts non-ASCII characters to escape sequences.
    Returns the result in string.
    """
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)

    return wrap

@escape_unicode
def northern_city():
    return 'Tromsø'
