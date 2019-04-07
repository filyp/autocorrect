import json
import re

from autocorrect.constants import word_regexes


def get_words(filename, lang): 
    word = word_regexes[lang]
    capitalized = r'(\.|^)\s*' + word_regexes[lang]
    with open(filename) as file: 
        for line in file: 
            line = re.sub(capitalized, '', line)
            for word in re.findall(word, line): 
                yield word


def parse(words):
    counts = dict()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


def count_words(src_filename, lang, out_filename='word_count.json'):
    words = get_words(src_filename, lang)
    counts = parse(words)
    with open(out_filename, 'w') as outfile:
        json.dump(counts, outfile)
