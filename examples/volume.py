# file: volume.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Author: R.F. Smith <rsmith@xs4all.nl>
# Created: 2017-07-09 17:56:24 +0200
# Last modified: 2017-07-09 18:05:46 +0200
#
# To the extent possible under law, R.F. Smith has waived all copyright and
# related or neighboring rights to volume.py. This work is published
# from the Netherlands. See http://creativecommons.org/publicdomain/zero/1.0/

from calculations import do

do('L = 1.2', 'm')
do('B = 0.5', 'm')
do('H = 0.23', 'm')
do('volume = L * B * H', 'm³')
