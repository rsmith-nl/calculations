# file: volume.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Copyright © 2017 R.F. Smith <rsmith@xs4all.nl>.
# SPDX-License-Identifier: MIT
# Created: 2017-07-09T17:56:24+0200
# Last modified: 2018-04-17T21:50:16+0200

from calculations import do

do('L = 1.2', 'm')
do('B = 0.5', 'm')
do('H = 0.23', 'm')
do('volume = L * B * H', 'm³')
