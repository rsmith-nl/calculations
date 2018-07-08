# file: calculations.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Copyright © 2017 R.F. Smith <rsmith@xs4all.nl>.
# SPDX-License-Identifier: MIT
# Created: 2017-07-09T17:02:43+0200
# Last modified: 2018-07-08T10:42:19+0200
"""Calculate and print Python expressions."""

_local_dict = {}


def do(expr, comment='', loc=_local_dict):
    """Process and print an assignment expression plus its result.

    Arguments:
        expr: Assignment expression to print.
        comment: Text to be printed after the assignment.
        loc: Dictionary of locals. Defaults to _local_dict.
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
        print(f'{expr} {comment}')
    except ValueError:
        k = newkeys.pop()
        print(f'{expr} = {loc[k]:.4g} {comment}')
