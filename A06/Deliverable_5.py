# -*- coding: utf-8 -*-

__author__ = "Anshul Kapoor(10456388)| " \
             "Pranay Singh(10455251) | " \
             "Himanshu Bishnoi(10451752)"

import nltk
from nltk.corpus import brown

"""
The lookup tagger is more accurate than the regex tagger. 
The regex taggers accuracy could be improved with better or 
more rules for the different tags. Applying embeddings would 
allow for more accurate tagging. A word embedding is a learned 
representation for text where words that have the same meaning 
have a similar representation. Words that have similar usages 
would have similar representations and therefore it is better 
at catching their meaning.
"""

# REGEX TAGGER
patterns = [
    (r'.*ing$', 'VBG'),
    (r'.*ed$', 'VBD'),  # simple past
    (r'.*es$', 'VBZ'),  # 3rd singular present
    (r'.*ould$', 'MD'),  # modals
    (r'.*\'s$', 'NN$'),  # possessive nouns
    (r'.*s$', 'NNS'),  # plural nouns
    (r'^-?[0-9]+(\.[0-9]+)?$', 'CD'),  # cardinal numbers
    (r'.*', 'NN')  # nouns (default)
]

def regexp_tagger_func(pattern, val):
    regexp_tagger = nltk.RegexpTagger(pattern)
    print(regexp_tagger.tag(nltk.tokenize.word_tokenize(val)))


def lookup_tagger_func(val):
    brown_tagged_sents = brown.tagged_sents()
    unigram_tagg = nltk.UnigramTagger(brown_tagged_sents)
    print(unigram_tagg.tag(nltk.tokenize.word_tokenize(val)))

def longestSentence():
    md = nltk.corpus.gutenberg.raw('melville-moby_dick.txt')
    sent_token = nltk.data.load('tokenizers/punkt/english.pickle')
    sent = sent_token.tokenize(md)

    val = ""
    word_count = 0
    for s in sent:
        w = len(nltk.tokenize.word_tokenize(s))
        if w > word_count:
            word_count = w
            val = s

    print("The word count is: " + str(word_count))
    print("The longest sentence is: \n" + val)

    return val


def main():
    """ Main function which is used as an interface """
    newVal = longestSentence()

    print("\n********* Regex Tagger *********")
    regexp_tagger_func(patterns, newVal)

    print("\n********* Lookup Tagger *********")
    lookup_tagger_func(newVal)


if __name__ == '__main__':
    main()
