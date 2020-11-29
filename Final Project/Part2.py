# -*- coding: utf-8 -*-

__author__ = "Anshul Kapoor(10456388)| " \
             "Pranay Singh(10455251) | " \
             "Himanshu Bishnoi(10451752)"

"""
Respond to and elaborate on Exercise 42, p128, in BKL.
.
.
.
.

Use WordNet to create a semantic index for a text collection.
Extend the con- cordance search program in Example 3-1,
indexing each word using the offset of its first synset,
e.g., wn.synsets('dog')[0].offset (and optionally the offset
of some of its ancestors in the hypernym hierarchy).

"""

import nltk
from nltk.corpus import wordnet as wn


class IndexedText(object):
    def __init__(self, stemmer, text):
        self._text = text
        self._stemmer = stemmer
        self._index = nltk.Index((self._stem(word), i)
                                 for (i, word) in enumerate(text))

    def concordance(self, word, width=40):
        key = self._stem(word)
        wc = int(width / 4)  # words of context
        for i in self._index[key]:
            left_context = ' '.join(self._text[i - wc:i])
            right_context = ' '.join(self._text[i:i + wc])
            offset = '(WordNet Offset: ' + str(wn.synsets(self._text[i])[0].offset()) + ')'
            left_display = '%*s' % (width, left_context[-width:])
            right_display = '%-*s' % (width, right_context[:width])
            print(left_display, right_display, offset)

    def _stem(self, word):
        return self._stemmer.stem(word).lower()


porter = nltk.PorterStemmer()
grail = nltk.corpus.webtext.words('grail.txt')
textToProcess = IndexedText(porter, grail)
textToProcess.concordance('lie')
