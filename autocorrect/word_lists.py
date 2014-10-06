# Python 3 Spelling Corrector
#
# Copyright 2014 Jonas McCallum.
# Updated for Python 3, based on Peter Norvig's
# 2007 version: http://norvig.com/spell-correct.html
#
# Open source, MIT license
# http://www.opensource.org/licenses/mit-license.php
"""
Word lists for case agnostic/pragmatic lookups

Author: Jonas McCallum
https://github.com/foobarmus/autocorrect

"""
from autocorrect.utils import words_from_archive

LOWERCASE = words_from_archive('en_US_GB_CA_lower.txt')
CASE_MAPPED = words_from_archive('en_US_GB_CA_mixed.txt', map_case=True)
