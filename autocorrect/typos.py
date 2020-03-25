# Python 3 Spelling Corrector
#
# Copyright 2014 Jonas McCallum.
# Updated for Python 3, based on Peter Norvig's
# 2007 version: http://norvig.com/spell-correct.html
"""
Word based methods and functions

Author: Jonas McCallum
https://github.com/foobarmus/autocorrect

Optimized by: Filip Sondej
https://github.com/fifimajster/autocorrect/

"""

from itertools import chain

from autocorrect.constants import alphabets


class Word(object):
    """container for word-based methods"""
    __slots__ = ['slices', 'word', 'alphabet']  # optimization

    def __init__(self, word, lang='en'):
        """
        Generate slices to assist with typo
        definitions.

        'the' => (('', 'the'), ('t', 'he'),
                  ('th', 'e'), ('the', ''))

        """
        slice_range = range(len(word) + 1)
        self.slices = tuple((word[:i], word[i:])
                            for i in slice_range)
        self.word = word
        self.alphabet = alphabets[lang]

    def _deletes(self):
        """th"""
        for a, b in self.slices[:-1]:
            yield ''.join((a, b[1:]))

    def _transposes(self):
        """teh"""
        for a, b in self.slices[:-2]:
            yield ''.join((a, b[1], b[0], b[2:]))

    def _replaces(self):
        """tge"""
        for a, b in self.slices[:-1]:
            for c in self.alphabet:
                yield ''.join((a, c, b[1:]))

    def _inserts(self):
        """thwe"""
        for a, b in self.slices:
            for c in self.alphabet:
                yield ''.join((a, c, b))

    def typos(self):
        """letter combinations one typo away from word"""
        return chain(self._deletes(),
                     self._transposes(),
                     self._replaces(),
                     self._inserts())

    def double_typos(self):
        """letter combinations two typos away from word"""
        return chain.from_iterable(
            Word(e1).typos() for e1 in self.typos())
