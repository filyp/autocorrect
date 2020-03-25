from __future__ import print_function

import json
import os
import re
import sys
import tarfile
from contextlib import closing

from autocorrect.constants import word_regexes
from autocorrect.typos import Word

if sys.version_info[0] == 3:
    from urllib.request import urlretrieve
else:
    from urllib import urlretrieve


PATH = os.path.abspath(os.path.dirname(__file__))
languages_url = "https://github.com/fsondej/autocorrect/raw/master/\
optional_languages/{}.tar.gz"


# credit: https://stackoverflow.com/questions/43370284/why-function-works-properly-without-specifying-parameters
class ProgressBar:
    def __init__(self):
        self.old_percent = 0
        print('_' * 50)

    def download_progress_hook(self, count, blockSize, totalSize):
        percent = int(count * blockSize * 100 / totalSize)
        if percent >= 2 + self.old_percent:
            self.old_percent = percent
            # print(percent, '%')
            print('>', end='')
            sys.stdout.flush()
        if percent == 100:
            print('\ndone!')


def load_from_tar(lang, file_name='word_count.json'):
    archive_name = os.path.join(PATH, 'data/{}.tar.gz'.format(lang))

    if not os.path.isfile(archive_name):
        print('dictionary for this language not found, downloading...')
        url = languages_url.format(lang)
        progress = ProgressBar()
        urlretrieve(url, archive_name, progress.download_progress_hook)

    with closing(tarfile.open(archive_name, 'r:gz')) as tarf:
        with closing(tarf.extractfile(file_name)) as file:
            return json.load(file)


class Speller:
    def __init__(self, threshold=0, lang='en'):
        self.threshold = threshold
        self.nlp_data = load_from_tar(lang)
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
        def get_candidates(word):
            w = Word(word, self.lang)
            candidates = (self.existing([word]) or
                          self.existing(w.typos()) or
                          self.existing(w.double_typos()) or
                          [word])
            return [(self.nlp_data.get(c), c) for c in candidates]

        candidates = get_candidates(word)

        # in case the word is capitalized
        if word[0].isupper():
            candidates += get_candidates(word.lower())

        best_word = max(candidates)[1]

        if word[0].isupper():
            best_word = best_word.capitalize()
        return best_word

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
        print('autocorrect.spell is deprecated, \
            use autocorrect.Speller instead')
        if self.speller is None:
            self.speller = Speller()
        return self.speller(sentence)


spell = LazySpeller()
