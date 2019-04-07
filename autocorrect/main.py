import json
import re
import tarfile
from contextlib import closing

from typos import Word


def load_from_tar(archive_name, file_name='word_count.json'):
    with closing(tarfile.open(archive_name, 'r:gz')) as tarf:
        with closing(tarf.extractfile(file_name)) as file:
            return json.load(file)


class Speller:
    def __init__(self, threshold=0):
        self.threshold = threshold
        self.nlp_data = load_from_tar('word_count.json.tar')

        # print(len(self.nlp_data))
        # self.nlp_data = {k: v for k, v in self.nlp_data.items() 
        #                 if v > threshold}
        # print(len(self.nlp_data))

    def existing(self, words):
        """{'the', 'teh'} => {'the'}"""
        # return set(words) & self.nlp_words
        return set(word for word in words
                    if word in self.nlp_data)

    def __call__(self, word):
        """most likely correction for everything up to a double typo"""
        w = Word(word, 'pl')
        candidates = (self.existing([word]) or 
                      self.existing(w.typos()) or 
                      self.existing(w.double_typos()) or 
                      [word])
        return max(candidates, key=self.nlp_data.get)
