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


def concat(*args):
    """reversed('th'), 'e' => 'hte'"""
    try:
        return ''.join(args)
    except TypeError:
        return ''.join(chain.from_iterable(args))


class Word(object):
    """container for word-based methods"""

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
        return (concat(a, b[1:])
                for a, b in self.slices[:-1])

    def _transposes(self):
        """teh"""
        return (concat(a, reversed(b[:2]), b[2:])
                for a, b in self.slices[:-2])

    def _replaces(self):
        """tge"""
        return (concat(a, c, b[1:])
                for a, b in self.slices[:-1]
                for c in self.alphabet)

    def _inserts(self):
        """thwe"""
        return (concat(a, c, b)
                for a, b in self.slices
                for c in self.alphabet)

    def typos(self):
        """letter combinations one typo away from word"""
        yield from self._deletes()
        yield from self._transposes()
        yield from self._replaces()
        yield from self._inserts()

    def double_typos(self):
        """letter combinations two typos away from word"""
        return (e2 for e1 in self.typos()
                for e2 in Word(e1).typos())
