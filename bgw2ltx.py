#!/usr/bin/python
"""
Format biblegateway copy-paste text to latex form.

Convert verse numbers within text to latexified verse numbers, for much nicer
display within polyglots etc.
"""
# Author: Andy Holt
# Date: Tue 24 Nov 2015 12:45
# Usage: ./bgw2ltx.py filename1 [filename2]

import sys
import re

for txt in sys.argv[1:]:
    # open txt file and extract text
    file = open(txt).read()

    # very stupid replacement, need to improve
    # [todo] - more intelligent verse number finder algorithm
    # currently will replace any numeric-string with a versified
    # version. Doesn't respect numbers within the text.
    latexifiedPassage = re.sub(r'([0-9]+)\s',
                               r'\\vn{\1}',
                               file)

    f = open(txt, 'w')
    f.write(latexifiedPassage)
    f.close
