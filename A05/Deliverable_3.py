# -*- coding: utf-8 -*-

__author__ = "Anshul Kapoor(10456388)| " \
             "Pranay Singh(10455251) | " \
             "Himanshu Bishnoi(10451752)"


import nltk
import nltk.corpus
from nltk.corpus import brown
from nltk.text import Text

def posTag():
    """ Your Turn Pg 180 Chapter 5 """
    print("\n*** Your Turn Pg 180 Chapter 5 Output ***")
    text = nltk.word_tokenize("I want to read. Good read!")
    print(nltk.pos_tag(text))

def tagged_words():
    """ Your Turn Pg 184 Chapter 5 """
    print("\n*** Your Turn Pg 184 Chapter 5 Output ***")
    brwn_news_tg = brown.tagged_words(categories='news', tagset='universal')
    tag_freq_dist = nltk.FreqDist(tag for (word, tag) in brwn_news_tg)
    tag_freq_dist.keys()
    tag_freq_dist.plot(cumulative=True)
    tag_freq_dist
    total = tag_freq_dist['NOUN'] + tag_freq_dist['DET'] + tag_freq_dist['PRT'] + tag_freq_dist['VERB'] + tag_freq_dist[
        'PRON']
    percent = 0
    for i in tag_freq_dist:
        percent = percent + tag_freq_dist[i]

    percnt = total * 100 / percent
    print(percnt)


def ConditionalFreqDist():
    """ Your Turn Pg 189 Chapter 5 """
    print("\n*** Your Turn Pg 189 Chapter 5 Output ***")
    wrd = nltk.corpus.gutenberg.words('chesterton-brown.txt')
    brwn_news_tggd = brown.tagged_words(categories='news', tagset='universal')
    d = nltk.ConditionalFreqDist((wrd.lower(), tag) for (wrd, tag) in brwn_news_tggd)
    txtlst = Text(wrd)
    for word in d.conditions():
        if len(d[word]) > 3:
            tags = d[word].keys()
            print(word, ' '.join(tags))

    for word in d.conditions():
        if len(d[word]) > 3:
            txtlst.concordance(word)


def main():
    """ Main function which is used as an interface """
    posTag()  # Your Turn Pg 180 Chapter 5
    tagged_words()  # Your Turn Pg 184 Chapter 5
    # FreqDist()  # Your Turn Pg 186 Chapter 5
    ConditionalFreqDist()  # Your Turn Pg 189 Chapter 5


if __name__ == '__main__':
    main()
