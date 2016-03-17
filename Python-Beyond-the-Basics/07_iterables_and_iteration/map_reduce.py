# -*- coding: utf-8 -*-

from pprint import pprint
from functools import reduce

def count_words(doc):
    normalized_doc = ''.join(c.lower() if c.isalpha() else ' ' for c in doc)
    frequencies = {}
    for word in normalized_doc.split():
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies


def combine_counts(d1, d2):
    d = d1.copy()
    for word, count in d2.items():
        d[word] = d.get(word, 0) + count
    return d


def main():
    documents = [
        'It was the best of times, it was the worst of times.',
        'I went to the woods because I wished to live deliberately, to front only ...',
        'Friends, Romans, countrymen, lend me your ears; I come to bury Caesar, not to ...',
        'I do not like green eggs and ham. I do not like them, Sam-I-Am.',
    ]
    counts = map(count_words, documents)

    total_counts = reduce(combine_counts, counts)
    pprint(total_counts)

if __name__ == '__main__':
    main()
