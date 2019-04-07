import re
import json

word_pl = r'[A-Za-zęóąśłżźćń]+' 


def get_words(filename): 
    with open(filename) as file: 
        for line in file: 
            for word in re.findall(word_pl, line): 
                yield word.lower() 


def parse(words):
    counts = dict()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


def count_words(src_filename, out_filename='word_count.json'):
    words = get_words(src_filename)
    counts = parse(words)
    with open(out_filename, 'w') as outfile:
        json.dump(counts, outfile)
