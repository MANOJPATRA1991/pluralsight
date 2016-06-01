# -*- coding: utf-8 -*-

from fractions import Fraction


def mixed_numeral(vulgar):

    # <BELOW IS NOT CONSIDER PYTHONIC>
    # if not (hasattr(vulgar, 'numerator') and hasattr(vulgar, 'denominator')):
    #     raise TypeError("{} is not a rational number".format(vulgar))

    try:
        integer = vulgar.numerator // vulgar.denominator
        fraction = Fraction(vulgar.numerator - integer * vulgar.denominator,
                            vulgar.denominator)
        return integer, fraction
    except AttributeError as e:
        raise TypeError("{} is not a rational number".format(vulgar)) from e
