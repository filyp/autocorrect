# Python 3 Spelling Corrector
#
# Copyright 2014 Jonas McCallum.
# Updated for Python 3, based on Peter Norvig's
# 2007 version: http://norvig.com/spell-correct.html
#
# Open source, MIT license
# http://www.opensource.org/licenses/mit-license.php
"""
Word lists for case sensitive/insensitive lookups

Author: Jonas McCallum
https://github.com/foobarmus/autocorrect

"""
from autocorrect.utils import words_from_archive

# en_US_GB_CA is a superset of US, GB and CA
# spellings (color, colour, etc). It contains
# roughly half a million words. For this
# example, imagine it's just seven words...
#
# we (lower)
# flew (lower)
# to (lower)
# Abu (mixed)
# Dhabi (mixed)
# via (lower)
# Colombo (mixed)

LOWERCASE = words_from_archive('en_US_GB_CA_lower.txt')
# {'we', 'flew', 'to', 'via'}

CASE_MAPPED = words_from_archive('en_US_GB_CA_mixed.txt',
                                 map_case=True)
#  {abu': 'Abu',
#  'dhabi': 'Dhabi',
#  'colombo': 'Colombo'}
#
# Note that en_US_GB_CA_mixed.txt also contains
# acronyms/mixed case variants of common words,
# so in reality, CASE_MAPPED also contains: 
#
# {'to': 'TO',
#  'via': 'Via'}

MIXED_CASE = set(CASE_MAPPED.values())
# {'Abu', 'Dhabi', 'Colombo'}

LOWERED = set(CASE_MAPPED.keys())
# {'abu', 'dhabi', 'colombo'}
