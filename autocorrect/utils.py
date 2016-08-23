# Python 3 Spelling Corrector
#
# Copyright 2014 Jonas McCallum.
# Updated for Python 3, based on Peter Norvig's
# 2007 version: http://norvig.com/spell-correct.html
#
# Open source, MIT license
# http://www.opensource.org/licenses/mit-license.php
"""
File reader, concat function and dict wrapper

Author: Jonas McCallum
https://github.com/foobarmus/autocorrect

"""
import re, os, tarfile
from contextlib import closing
from itertools import chain

PATH = os.path.abspath(os.path.dirname(__file__))
BZ2 = 'words.bz2'
RE = '[A-Za-z]+'

def words_from_archive(filename, include_dups=False, map_case=False):
    """extract words from a text file in the archive"""
    bz2 = os.path.join(PATH, BZ2)
    tar_path = '{}/{}'.format('words', filename)
    with closing(tarfile.open(bz2, 'r:bz2')) as t:
        with closing(t.extractfile(tar_path)) as f:
            words = re.findall(RE, f.read().decode(encoding='utf-8'))
    if include_dups:
        return words
    elif map_case:
        return {w.lower():w for w in words}
    else:
        return set(words)

def concat(*args):
    """reversed('th'), 'e' => 'hte'"""
    try:
        return ''.join(args)
    except TypeError:
        return ''.join(chain.from_iterable(args))

class Zero(dict):
    """dict with a zero default"""

    def __getitem__(self, key):
        return self.get(key)

    def get(self, key):
        try:
            return super(Zero, self).__getitem__(key)
        except KeyError:
            return 0

zero_default_dict = Zero
