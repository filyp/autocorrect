import json
import re
import tarfile
import os
from contextlib import closing

from autocorrect.constants import word_regexes
from autocorrect.typos import Word

PATH = os.path.abspath(os.path.dirname(__file__))


def load_from_tar(archive_name, file_name='word_count.json'):
    with closing(tarfile.open(archive_name, 'r:gz')) as tarf:
        with closing(tarf.extractfile(file_name)) as file:
            return json.load(file)


class Speller:
    def __init__(self, threshold=0, lang='en'):
        self.threshold = threshold
        tarfile = os.path.join(PATH, 
                               'data/{}.tar.gz'.format(lang))
        self.nlp_data = load_from_tar(tarfile)
        self.lang = lang

        if threshold > 0:
            print('Original number of words: {}'
                    .format(len(self.nlp_data)))
            self.nlp_data = {k: v for k, v in self.nlp_data.items() 
                            if v > threshold}
            print('After applying threshold: {}'
                    .format(len(self.nlp_data)))

    def existing(self, words):
        """{'the', 'teh'} => {'the'}"""
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


# for backward compatibility
class LazySpeller:
    def __init__(self):
        self.speller = None
    
    def __call__(self, sentence):
        print('autocorrect.spell is deprecated, use autocorrect.Speller instead')
        if self.speller is None:
            self.speller = Speller()
        return self.speller(sentence)

spell = LazySpeller()
