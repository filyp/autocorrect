import json
import re
from collections import Counter, OrderedDict

from autocorrect.constants import word_regexes


def get_words(filename, lang):
    word_regex = word_regexes[lang]
    capitalized_regex = r'(\.|^|<|"|\'|\(|\[|\{)\s*' + word_regexes[lang]
    with open(filename) as file:
        for line in file:
            line = re.sub(capitalized_regex, '', line)
            for word in re.findall(word_regex, line):
                yield word


def count_words(src_filename, lang, out_filename='word_count.json'):
    words = get_words(src_filename, lang)
    counts = Counter(words)
    # make output file human readable
    counts_list = list(counts.items())
    counts_list.sort(key=lambda i: counts[i[0]], reverse=True)
    counts_ord_dict = OrderedDict(counts_list)
    with open(out_filename, 'w') as outfile:
        json.dump(counts_ord_dict, outfile, indent=4)
