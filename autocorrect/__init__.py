import json
import os
import re
import sys
import tarfile
import textwrap
from contextlib import closing
from urllib.request import urlretrieve

from autocorrect.constants import word_regexes, backup_urls, ipfs_gateways, ipfs_paths
from autocorrect.typos import Word

PATH = os.path.abspath(os.path.dirname(__file__))


# credit: https://stackoverflow.com/questions/43370284
class ProgressBar:
    def __init__(self):
        self.old_percent = 0
        print("_" * 50)

    def download_progress_hook(self, count, blockSize, totalSize):
        percent = int(count * blockSize * 100 / totalSize)
        if percent >= 2 + self.old_percent:
            self.old_percent = percent
            # print(percent, '%')
            print(">", end="")
            sys.stdout.flush()
        if percent == 100:
            print("\ndone!")


def load_from_tar(lang, file_name="word_count.json"):
    archive_name = os.path.join(PATH, f"data/{lang}.tar.gz")

    if lang not in word_regexes:
        supported_langs = ", ".join(word_regexes.keys())
        raise NotImplementedError(
            textwrap.dedent(
                f"""
            language '{lang}' not supported
            supported languages: {supported_langs}
            you can easily add new languages by following instructions at
            https://github.com/fsondej/autocorrect/tree/master#adding-new-languages
            """
            )
        )

    if not os.path.isfile(archive_name):
        print("dictionary for this language not found, downloading...")
        urls = [
            gateway + path for gateway in ipfs_gateways for path in ipfs_paths[lang]
        ]
        if lang in backup_urls:
            urls += backup_urls[lang]
        for url in urls:
            progress = ProgressBar()
            try:
                urlretrieve(url, archive_name, progress.download_progress_hook)
                error_message = None
                break
            except Exception as ex:
                print(f"couldn't download {url}, trying next url...")
                error_message = str(ex)
        if error_message is not None:
            raise ConnectionError(
                error_message
                + "\nFix your network connection, or manually download \n{}"
                "\nand put it in \nPATH_TO_REPO/autocorrect/data/".format(url)
            )

    with closing(tarfile.open(archive_name, "r:gz")) as tarf:
        with closing(tarf.extractfile(file_name)) as file:
            return json.load(file)


class Speller:
    def __init__(
        self, lang="en", threshold=0, nlp_data=None, fast=False, only_replacements=False
    ):
        self.lang = lang
        self.threshold = threshold
        self.nlp_data = load_from_tar(lang) if nlp_data is None else nlp_data
        self.fast = fast
        self.only_replacements = only_replacements

        if threshold > 0:
            # print(f'Original number of words: {len(self.nlp_data)}')
            self.nlp_data = {k: v for k, v in self.nlp_data.items() if v >= threshold}
            # print(f'After applying threshold: {len(self.nlp_data)}')

    def existing(self, words):
        """{'the', 'teh'} => {'the'}"""
        return {word for word in words if word in self.nlp_data}

    def get_candidates(self, word):
        w = Word(word, self.lang, self.only_replacements)
        if self.fast:
            candidates = self.existing([word]) or self.existing(w.typos()) or [word]
        else:
            candidates = (
                self.existing([word])
                or self.existing(w.typos())
                or self.existing(w.double_typos())
                or [word]
            )
        return [(self.nlp_data.get(c, 0), c) for c in candidates]

    def autocorrect_word(self, word):
        """most likely correction for everything up to a double typo"""
        if word == "":
            return ""

        candidates = self.get_candidates(word)

        # in case the word is capitalized
        if word[0].isupper():
            decapitalized = word[0].lower() + word[1:]
            candidates += self.get_candidates(decapitalized)

        best_word = max(candidates)[1]

        if word[0].isupper():
            best_word = best_word[0].upper() + best_word[1:]
        return best_word

    def autocorrect_sentence(self, sentence):
        return re.sub(
            word_regexes[self.lang],
            lambda match: self.autocorrect_word(match.group(0)),
            sentence,
        )

    __call__ = autocorrect_sentence


# for backward compatibility
class LazySpeller:
    def __init__(self):
        self.speller = None

    def __call__(self, sentence):
        print(
            "autocorrect.spell is deprecated, \
            use autocorrect.Speller instead"
        )
        if self.speller is None:
            self.speller = Speller()
        return self.speller(sentence)


spell = LazySpeller()
