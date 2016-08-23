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
from autocorrect.utils import concat
from autocorrect.nlp_parser import NLP_WORDS
from autocorrect.word_lists import LOWERCASE, MIXED_CASE
from autocorrect.word_lists import LOWERED, CASE_MAPPED

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
KNOWN_WORDS = LOWERCASE | LOWERED | NLP_WORDS

class Word(object):
    """container for word-based methods"""

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
                for c in ALPHABET}

    def _inserts(self):
        """thwe"""
        return {concat(a, c, b)
                for a, b in self.slices
                for c in ALPHABET}

    def typos(self):
        """letter combinations one typo away from word"""
        return (self._deletes() | self._transposes() |
                self._replaces() | self._inserts())

    def double_typos(self):
        """letter combinations two typos away from word"""
        return {e2 for e1 in self.typos()
                for e2 in Word(e1).typos()}


def common(words):
    """{'the', 'teh'} => {'the'}"""
    return set(words) & NLP_WORDS

def exact(words):
    """{'Snog', 'snog', 'Snoddy'} => {'Snoddy'}"""
    return set(words) & MIXED_CASE

def known(words):
    """{'Gazpacho', 'gazzpacho'} => {'gazpacho'}"""
    return {w.lower() for w in words} & KNOWN_WORDS

def known_as_lower(words):
    """{'Natasha', 'Bob'} => {'bob'}"""
    return {w.lower() for w in words} & LOWERCASE

def get_case(word, correction):
    """
    Best guess of intended case.

    manchester => manchester
    chilton => Chilton
    AAvTech => AAvTech
    THe => The
    imho => IMHO

    """
    if word.istitle():
        return correction.title()
    if word.isupper():
        return correction.upper()
    if correction == word and not word.islower():
        return word
    if len(word) > 2 and word[:2].isupper():
        return correction.title()
    if not known_as_lower([correction]): #expensive
        try:
            return CASE_MAPPED[correction]
        except KeyError:
            pass
    return correction
