import json
import re
import tarfile
from contextlib import closing

from typos import Word


def load_from_tar(archive_name, file_name):
    with closing(tarfile.open(archive_name, 'r:gz')) as tarf:
        with closing(tarf.extractfile(file_name)) as file:
            return json.load(file)


class Speller:
    def __init__(self, threshold=0):
        self.threshold = threshold
        self.nlp_data = load_from_tar('word_count.json.tar', 'word_count.json')
        self.nlp_words = self.nlp_data.keys()

    def existing(self, words):
        """{'the', 'teh'} => {'the'}"""
        return set(words) & self.nlp_words

    def __call__(self, word):
        """most likely correction for everything up to a double typo"""
        w = Word(word)
        candidates = (self.existing([word]) or 
                      self.existing(w.typos()) or 
                      self.existing(w.double_typos()) or 
                      [word])
        return max(candidates, key=self.nlp_data.get)
