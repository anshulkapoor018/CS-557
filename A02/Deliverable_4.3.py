import nltk
import pandas as pd
from nltk.util import ngrams

# Corpus 1 === Monty Python and the Holy Grail Corpus
e_text = nltk.corpus.webtext.words('grail.txt')
e_unigram = ngrams(e_text, 1)
e_bigrams = ngrams(e_text, 2)

# Corpus 2 === Personals Corpus
m_text = nltk.corpus.webtext.words('singles.txt')
m_unigram = ngrams(m_text, 1)
m_bigrams = nltk.bigrams(m_text)

# Computing Frequency Distributions for Unigrams
emma_dist_unigrams = nltk.FreqDist(e_unigram)
moby_dist_unigrams = nltk.FreqDist(m_unigram)

# Computing Frequency Distributions for Bigrams
emma_dist_bigrams = nltk.FreqDist(e_bigrams)
moby_dist_bigrams = nltk.FreqDist(m_bigrams)

unigrams_count = 0
bigrams_count = 0

# Creating a dataframe
cols = ['Key', 'Corpus 1 Value', 'Corpus 2 value']
result_unigrams = pd.DataFrame(columns=cols)
result_bigrams = pd.DataFrame(columns=cols)

# Comparing unigrams of two corpus
for key1, value1 in emma_dist_unigrams.items():
    for key2, value2 in moby_dist_unigrams.items():
        if key1 == key2:
            result_unigrams.loc[unigrams_count] = [key1, value1, value2]
            unigrams_count = unigrams_count + 1

# Comparing bigrams of two corpus
for key3, value3 in emma_dist_bigrams.items():
    for k4, v4 in moby_dist_bigrams.items():
        if key3 == k4:
            result_bigrams.loc[bigrams_count] = [key3, value3, v4]
            bigrams_count = bigrams_count + 1

result_unigrams = result_unigrams.sort_values('Corpus 1 Value')
print(result_unigrams[-5:][:])

result_bigrams = result_bigrams.sort_values('Corpus 1 Value')
print(result_bigrams[-5:][:])
print("End")

# Calculate Perplexity for unigrams
perplexity = 1
N = 1
x = 0

text = "ARTHUR : Then I dub you Sir Bedevere , Knight of the Round Table NARRATOR : The wise Sir Bedevere was the first to join King Arthur ' s knights , but other illustrious names were soon to follow : Sir Lancelot the Brave ; Sir Gallahad the Pure ; and Sir Robin the - not - quite - so - brave - as - Sir - Lancelot , who had nearly fought the Dragon of Angnor , who had nearly stood up to the vicious Chicken of Bristol , and who had personally wet himself at the Battle of Badon Hill ; and the aptly named Sir Not - appearing - in - this - film ."
test_set = nltk.word_tokenize(text)

for w in test_set:
    if w in result_unigrams:
        N = N + 1
        perplexity = perplexity * (1 / result_unigrams[x])
    x = x + 1

perplexity = pow(perplexity, 1 / float(N))
