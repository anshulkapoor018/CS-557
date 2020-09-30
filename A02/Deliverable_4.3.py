import nltk
import pandas as pd
from nltk.util import ngrams
def main():  

    y = nltk.corpus.webtext.words('grail.txt')
    e_uni = ngrams(y, 1)
    e_bi = ngrams(y, 2)

    q = nltk.corpus.webtext.words('singles.txt')
    w = ngrams(q, 1)
    e = nltk.bigrams(q)

    # here we compute freq distributions for unigrams
    z = nltk.FreqDist(e_uni)
    o = nltk.FreqDist(w)

    # Similarly freq distributions for bigrams
    d = nltk.FreqDist(e_bi)
    l = nltk.FreqDist(e)

    cols = ['Key', 'Corpus 1 Value', 'Corpus 2 value']
    unigrams_res = pd.DataFrame(columns=cols)
    bigrams_res = pd.DataFrame(columns=cols)

    unigrams_res = compare_u(z,o, unigrams_res)
    unigrams_res = unigrams_res.sort_values('Corpus 1 Value')
    print(unigrams_res[-5:][:])

    bigrams_res = compare_b(d, l, bigrams_res)
    bigrams_res = bigrams_res.sort_values('Corpus 1 Value')
    print(bigrams_res[-5:][:])
    print("End")

    # here we calculate perplexity of unigrams
    per = 1
    N = 1
    x = 0

    text = "ARTHUR : Then I dub you Sir Bedevere , Knight of the Round Table NARRATOR : The wise Sir Bedevere was the first to join King Arthur ' s knights , but other illustrious names were soon to follow : Sir Lancelot the Brave ; Sir Gallahad the Pure ; and Sir Robin the - not - quite - so - brave - as - Sir - Lancelot , who had nearly fought the Dragon of Angnor , who had nearly stood up to the vicious Chicken of Bristol , and who had personally wet himself at the Battle of Badon Hill ; and the aptly named Sir Not - appearing - in - this - film ."
    test_set = nltk.word_tokenize(text)

    for w in test_set:
        if w in unigrams_res:
            N = N + 1
            per = per * (1 / unigrams_res[x])
        x = x + 1

    per = pow(per, 1 / float(N))


def compare_u(z, o, unigrams_res):
    unigrams_count = 0
    for key1, value1 in z.items():
        for key2, value2 in o.items():
            if key1 == key2:
                unigrams_res.loc[unigrams_count] = [key1, value1, value2]
                unigrams_count = unigrams_count + 1
    return unigrams_res


def compare_b(d, l, bigrams_res):
    bigrams_count = 0    
    for key3, value3 in d.items():
        for k4, v4 in l.items():
            if key3 == k4:
                bigrams_res.loc[bigrams_count] = [key3, value3, v4]
                bigrams_count = bigrams_count + 1
    return bigrams_res



if __name__ == '__main__':
    main()

