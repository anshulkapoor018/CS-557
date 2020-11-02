# -*- coding: utf-8 -*-

__author__ = "Anshul Kapoor(10456388)| " \
             "Pranay Singh(10455251) | " \
             "Himanshu Bishnoi(10451752)"

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import gutenberg


def sentence_tokenizer(textFile):
    wrd = gutenberg.words(textFile)
    print(f"Name of the corpus is: {textFile}")
    book = ''
    for word in wrd:
        book = book + word + ' '
    sentences = sent_tokenize(book)
    word_count = lambda sentence: len(word_tokenize(sentence))
    longestsentence = max(sentences, key=word_count)
    print('\nLongest sentence found using sentence tokenizer\n', longestsentence)
    print('\nLength of the above sentence: ', len(longestsentence))
    sentences = book.split(". ")
    longest_sent = max(sentences, key=len)
    print('\nLongest sentence between two consecutive periods\n', longest_sent)
    print('\nLength of the above sentence: ', len(longest_sent))


def main():
    """ Main function which is used as an interface """
    sentence_tokenizer("carroll-alice.txt")
    sentence_tokenizer("bryant-stories.txt")
    sentence_tokenizer("burgess-busterbrown.txt")


if __name__ == '__main__':
    main()
