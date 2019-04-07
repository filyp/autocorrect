import json
import re
import tarfile
from contextlib import closing

from autocorrect.constants import word_regexes
from autocorrect.typos import Word


def load_from_tar(archive_name, file_name='word_count.json'):
    with closing(tarfile.open(archive_name, 'r:gz')) as tarf:
        with closing(tarf.extractfile(file_name)) as file:
            return json.load(file)


class Speller:
    def __init__(self, threshold=0, lang='en'):
        self.threshold = threshold
        tarfile = f'data/{lang}wiki.tar.gz'
        self.nlp_data = load_from_tar(tarfile)
        self.lang = lang

        # print(len(self.nlp_data))
        # self.nlp_data = {k: v for k, v in self.nlp_data.items() 
        #                 if v > threshold}
        # print(len(self.nlp_data))

    def existing(self, words):
        """{'the', 'teh'} => {'the'}"""
        # return set(words) & self.nlp_words
        return set(word for word in words
                   if word in self.nlp_data)

    def autocorrect_word(self, word):
        """most likely correction for everything up to a double typo"""
        w = Word(word, self.lang)
        candidates = (self.existing([word]) or 
                      self.existing(w.typos()) or 
                      self.existing(w.double_typos()) or 
                      [word])
        return max(candidates, key=self.nlp_data.get)

    def autocorrect_sentence(self, sentence):
        return re.sub(word_regexes[self.lang],
                      lambda match: self.autocorrect_word(match.group(0)),
                      sentence)

    __call__ = autocorrect_sentence
