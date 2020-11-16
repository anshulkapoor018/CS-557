# -*- coding: utf-8 -*-

__author__ = "Anshul Kapoor(10456388)| " \
             "Pranay Singh(10455251) | " \
             "Himanshu Bishnoi(10451752)"

"""
J&M 3rd Exercise 11.1 
"""

from stat_parser import Parser
import nltk

moby_dick = nltk.corpus.gutenberg.raw('melville-moby_dick.txt')
sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
sentences = sent_tokenizer.tokenize(moby_dick)

def find_longest_sentence():
    longest_sentence = ""
    word_count = 0
    for sent in sentences:
        w = len(nltk.tokenize.word_tokenize(sent))
        if w > word_count:
            word_count = w
            longest_sentence = sent

    # print("longest sentence: \n" + longest_sentence)
    return longest_sentence

def main():
    """ Main function which is used as an interface """
    parser = Parser()
    sentence = "Book the cooks who cook the books."
    longest_sentence = find_longest_sentence()
    print(parser.parse(sentence))


if __name__ == '__main__':
    main()
