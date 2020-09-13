import json
import re
from collections import Counter, OrderedDict

from autocorrect.constants import word_regexes


def get_words(filename, lang, encd):
    word_regex = word_regexes[lang]
    capitalized_regex = r'(\.|^|<|"|\'|\(|\[|\{)\s*' + word_regexes[lang]
    with open(filename, encoding=encd) as file:
        for line in file:
            line = re.sub(capitalized_regex, '', line)
            yield from re.findall(word_regex, line)


def count_words(src_filename, lang, encd=None, out_filename='word_count.json'):
    words = get_words(src_filename, lang, encd)
    counts = Counter(words)
    # make output file human readable
    counts_list = list(counts.items())
    counts_list.sort(key=lambda i: i[1], reverse=True)
    counts_ord_dict = OrderedDict(counts_list)
    with open(out_filename, 'w') as outfile:
        json.dump(counts_ord_dict, outfile, indent=4)
