# -*- coding: utf-8 -*-

__author__ = "Anshul Kapoor(10456388)| " \
             "Pranay Singh(10455251) | " \
             "Himanshu Bishnoi(10451752)"

import re
from gensim.models import Word2Vec
from nltk.corpus import gutenberg
from scipy import spatial


def cosine_similarity(v1, v2):
    """ Define a function that computes
    cosine similarity between two words """
    return 1 - spatial.distance.cosine(v1, v2)

def importing_dataset():
    sent = list(gutenberg.sents('shakespeare-hamlet.txt'))  # convert into a list
    print('Type of corpus: ', type(sent))
    print('Length of corpus: ', len(sent))
    print(sent[0])
    print(sent[9])
    return sent

def main():
    """ Main function which is used as an interface """
    sent = importing_dataset()  # Import dataset

    # Clean the dataset
    for i in range(len(sent)):
        sent[i] = [word.lower() for word in sent[i] if re.match('^[a-zA-Z]+', word)]
    print(sent[0])
    print(sent[10])

    # Create a Word2Vec model
    model = Word2Vec(sentences=sent, size=100, sg=1, window=3, min_count=1, iter=10, workers=4)
    model.init_sims(replace=True)

    # Test
    model.wv.most_similar(sent[10])
    v1 = model.wv.__getitem__('king')
    v2 = model.wv.__getitem__('queen')

    print("Cosine Similarity of 'king' and 'queen': ", cosine_similarity(v1, v2))


if __name__ == '__main__':
    main()
