# -*- coding: utf-8 -*-
import nltk
import random
from nltk.corpus import senseval

instances = senseval.instances('hard.pos')


def features(instance):
    feat = dict()
    p = instance.position
    # previous word and tag
    if p:
        feat['wp'] = instance.context[p - 1][0]
        feat['tp'] = instance.context[p - 1][1]
    # use BOS if it is the first word
    else:  #
        feat['wp'] = (p, 'BOS')
        feat['tp'] = (p, 'BOS')
        # following word and tag
        feat['wf'] = instance.context[p + 1][0]
        feat['tf'] = instance.context[p + 1][1]
    return feat

def main():
    """ Main function which is used as an interface """

    # size = int(len(instances) * 0.1)
    # train_set, test_set = instances[size:], instances[:size]

    # Accessing instances
    for inst in senseval.instances('interest.pos')[:10]:
        p = inst.position
        left = ' '.join(w for (w, t) in inst.context[p - 2:p])
        word = ' '.join(w for (w, t) in inst.context[p:p + 1])
        right = ' '.join(w for (w, t) in inst.context[p + 1:p + 3])
        senses = ' '.join(inst.senses)
        print('%20s |%10s | %-15s -> %s' % (left, word, right, senses))

    feature_set = [(features(i), i.senses[0])
                   for i in instances if len(i.senses) == 1]

    random.shuffle(feature_set)  # shuffle them randomly

    print(feature_set[:2])
    # [({'tf': 'NNS', 'wf': 'rates', 'tp': 'IN', 'wp': 'in'}, 'interest_6'),
    # ({'tf': 'NNS', 'wf': 'rates', 'tp': 'VBG', 'wp': 'declining'},
    # 'interest_6')]

    # Small Samples
    train_set = feature_set[1500:]
    dev_set = feature_set[:1000]
    test_set = feature_set[1000:1500]
    # train, dev, test = feature_set[500:], feature_set[:250], feature_set[250:500]  # try on a small sample
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    print("Accuracy on Dev:", nltk.classify.accuracy(classifier, dev_set))
    print("Accuracy on Test:", nltk.classify.accuracy(classifier, train_set))


if __name__ == '__main__':
    main()
