# file: volume.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Author: R.F. Smith <rsmith@xs4all.nl>
# Created: 2017-07-09 17:56:24 +0200
# Last modified: 2017-07-09 18:00:13 +0200


from calculations import do

do('L = 1.2', 'm')
do('B = 0.5', 'm')
do('H = 0.23', 'm')
do('volume = L * B * H', 'm³')
