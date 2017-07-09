# file: calculations.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Author: R.F. Smith <rsmith@xs3all.nl>
# Created: 2016-07-05 01:15:25 +0200
# Last modified: 2017-07-09 18:07:08 +0200
#
# To the extent possible under law, R.F. Smith has waived all copyright and
# related or neighboring rights to calculations.py. This work is published
# from the Netherlands. See http://creativecommons.org/publicdomain/zero/1.0/

"""Calculate and print Python expressions."""

_local_dict = {}


def do(expr, comment='', loc=_local_dict):
    """Process and print an assignment expression plus its result.

    Arguments:
        expr: Assignment expression to print.
        comment: Text to be printed after the assignment.
        loc: Dictionary of locals. Defaults to local_dict.
    """
    before = set(loc.keys())
    exec(expr, None, loc)
    after = set(loc.keys())
    newkeys = after - before
    n = len(newkeys)
    if n == 0:
        raise ValueError('not an assignment')
    elif n > 1:
        raise ValueError('multiple assignemt')
    try:
        v = float(expr.split('=')[1])
        del v
        print('{} {}'.format(expr, comment))
    except ValueError:
        k = newkeys.pop()
        print('{} = {:.4g} {}'.format(expr, loc[k], comment))
