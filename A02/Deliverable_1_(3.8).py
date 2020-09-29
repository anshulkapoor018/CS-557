#!/user_id/bin/env python

"""
Deliverable_1_(3.8).py
"""
__author__ = "Anshul Kapoor"

# import nltk
# nltk.download('words')
from nltk.corpus import words
from collections import Counter


def print_anagram(word, dictionary, answer, output):
    count1 = Counter(word)
    for word_from_dict in dictionary:
        if Counter(word_from_dict) == count1:
            answer.append(word_from_dict)
    for anagram in answer:
        if anagram not in output:
            output.append(anagram)
    return output


def main():
    """ Main function which is used as an interface """
    dictionary = words.words()
    # print(dictionary)
    ans = []
    output = []
    word_check = input("Enter a word to print out possible anagrams: ")
    anagrams = print_anagram(word_check, dictionary, ans, output)
    print("***** Below are the anagrams of the given word *****\n")
    print(anagrams)


if __name__ == '__main__':
    main()
