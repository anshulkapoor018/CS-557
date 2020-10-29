# -*- coding: utf-8 -*-

__author__ = "Anshul Kapoor(10456388)| " \
             "Pranay Singh(10455251) | " \
             "Himanshu Bishnoi(10451752)"

import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
# import xlrd

def logit_regression(data):
    data = pd.read_excel(data)  # Reading Dataset provided
    X = data.iloc[:, [0, 1, 2]].values
    y = data.iloc[:, 3].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

    classifier = LogisticRegression(random_state=0, solver='liblinear', max_iter=1000)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    print('\nAccuracy Percentage:', np.mean(y_pred == y_test))
    cm = confusion_matrix(y_test, y_pred)
    print('\nConfusion Matrix:\n', cm)

def main():
    """ Main function which is used as an interface """
    data_source = 'RFMdataMPJ.xlsx'
    logit_regression(data_source)


if __name__ == '__main__':
    main()
