# file: volume.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Copyright © 2017 R.F. Smith <rsmith@xs4all.nl>.
# SPDX-License-Identifier: MIT
# Created: 2017-07-09T17:56:24+0200
# Last modified: 2018-07-08T11:08:09+0200

try:
    from calculations import do
except ImportError:
    import sys
    import os

    # This is a hack to enable the import to work
    sys.path[0] = os.path.dirname(sys.path[0])
    from calculations import do

do("L = 1.2", "m")
do("B = 0.5", "m")
do("H = 0.23", "m")
do("volume = L * B * H", "m³")
