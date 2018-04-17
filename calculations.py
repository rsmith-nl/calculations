# file: calculations.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Copyright © 2017 R.F. Smith <rsmith@xs4all.nl>.
# SPDX-License-Identifier: MIT
# Created: 2017-07-09T17:02:43+0200
# Last modified: 2018-04-17T21:48:54+0200
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
