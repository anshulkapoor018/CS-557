# -*- coding: utf-8 -*-

__author__ = "Anshul Kapoor(10456388)| " \
             "Pranay Singh(10455251) | " \
             "Himanshu Bishnoi(10451752)"

import numpy as np
import pandas as pd
import nltk.sentiment.util
import gzip
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression

def parse(path):
    v = gzip.open(path, 'rb')
    for b in v:
        yield eval(b)

def Df(path):
    idx = 0
    d = {}
    for f in parse(path):
        d[idx] = f
        idx += 1
    return pd.DataFrame.from_dict(d, orient='index')

def main():
    """ Main function which is used as an interface """
    amz = Df('reviews_Musical_Instruments_5.json.gz')

    negative_sentence = open("negative.txt").read()
    neg_words = negative_sentence.split('\n')

    positive_sentence = open("positive.txt").read()
    pos_words = positive_sentence.split('\n')

    df = pd.DataFrame(amz['reviewText'])
    df['positive_count'] = 0
    df['negative_count'] = 0
    df['negator_count'] = 0
    df['tags'] = amz['overall'].astype(int)

    for i in range(len(df)):
        pos_cnt = 0
        neg_cnt = 0
        negator_cnt = 0
        text = df.iloc[i, 0]
        words = text.split(' ')
        res = nltk.sentiment.util.mark_negation(text.split())

        for word in words:
            if word in pos_words:
                pos_cnt = pos_cnt + 1
            if word in neg_words:
                neg_cnt = neg_cnt + 1

        for word in res:
            if word.endswith('_NEG'):
                negator_cnt = negator_cnt + 1

        df.iloc[i, 1] = pos_cnt
        df.iloc[i, 2] = neg_cnt
        df.iloc[i, 3] = negator_cnt

    X = df.iloc[:, 1:4]
    Y = df.iloc[:, 4]

    scalar = preprocessing.StandardScaler()
    X = scalar.fit_transform(X)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=0)

    lr = LogisticRegression(multi_class='multinomial', solver='sag', max_iter=5000)
    print(lr.fit(X_train, Y_train))

    Y_pred = lr.predict(X_test)
    print("Accuracy on testing set: ", np.mean(Y_pred == Y_test))

    print("Accuracy on whole Dataset: ", lr.score(X, Y))

    con_mat = confusion_matrix(Y_test, Y_pred)
    print("Confusion matrix: \n", con_mat)


if __name__ == '__main__':
    main()
