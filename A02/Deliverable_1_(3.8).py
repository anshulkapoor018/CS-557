import nltk
nltk.download('words')
from nltk.corpus import words
from collections import Counter
dictionary = words.words()
ans = []
output = []
def printanagram(word , dictionary):
    count1 = Counter(word)
    for wordfromdict in dictionary:
       if Counter(wordfromdict)== count1:
           ans.append(wordfromdict)
    for anagram in ans:
        if anagram not in output:
            output.append(anagram) 
    return output

word_check = input("Enter a word to print out possible anagrams: ")
print("The anagrams of the given word is: \n")
anagrams = printanagram(word_check, dictionary)
print(anagrams)














 