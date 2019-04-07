# Python 3 Spelling Corrector
#
# Copyright 2014 Jonas McCallum.
# Updated for Python 3, based on Peter Norvig's
# 2007 version: http://norvig.com/spell-correct.html
#
# Open source, MIT license
# http://www.opensource.org/licenses/mit-license.php
"""
Word based methods and functions

Author: Jonas McCallum
https://github.com/foobarmus/autocorrect

"""

from itertools import chain


def concat(*args):
    """reversed('th'), 'e' => 'hte'"""
    try:
        return ''.join(args)
    except TypeError:
        return ''.join(chain.from_iterable(args))


class Word(object):
    """container for word-based methods"""

    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

    def __init__(self, word):
        """
        Generate slices to assist with typo
        definitions.

        'the' => (('', 'the'), ('t', 'he'),
                  ('th', 'e'), ('the', ''))

        """
        word_ = word.lower()
        slice_range = range(len(word_) + 1)
        self.slices = tuple((word_[:i], word_[i:])
                            for i in slice_range)
        self.word = word

    def _deletes(self):
        """th"""
        return {concat(a, b[1:])
                for a, b in self.slices[:-1]}

    def _transposes(self):
        """teh"""
        return {concat(a, reversed(b[:2]), b[2:])
                for a, b in self.slices[:-2]}

    def _replaces(self):
        """tge"""
        return {concat(a, c, b[1:])
                for a, b in self.slices[:-1]
                for c in self.ALPHABET}

    def _inserts(self):
        """thwe"""
        return {concat(a, c, b)
                for a, b in self.slices
                for c in self.ALPHABET}

    def typos(self):
        """letter combinations one typo away from word"""
        return (self._deletes() | self._transposes() |
                self._replaces() | self._inserts())

    def double_typos(self):
        """letter combinations two typos away from word"""
        return {e2 for e1 in self.typos()
                for e2 in Word(e1).typos()}