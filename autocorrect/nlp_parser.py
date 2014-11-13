# Python 3 Spelling Corrector
#
# Copyright 2014 Jonas McCallum.
# Updated for Python 3, based on Peter Norvig's
# 2007 version: http://norvig.com/spell-correct.html
#
# Open source, MIT license
# http://www.opensource.org/licenses/mit-license.php
"""
NLP parser

Author: Jonas McCallum
https://github.com/foobarmus/autocorrect

"""
from autocorrect.utils import words_from_archive, zero_default_dict

def parse(lang_sample):
    """tally word popularity using novel extracts, etc"""
    words = words_from_archive(lang_sample, include_dups=True)
    counts = zero_default_dict()
    for word in words:
        counts[word] += 1
    return set(words), counts

NLP_WORDS, NLP_COUNTS = parse('big.txt')
