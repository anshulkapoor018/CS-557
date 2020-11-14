# -*- coding: utf-8 -*-

__author__ = "Anshul Kapoor(10456388)| " \
             "Pranay Singh(10455251) | " \
             "Himanshu Bishnoi(10451752)"

import nltk

"""
    Words that can be used as a verb or noun with same pronunciation:
    - tag
    - book
    - view
    - quiet
    - cover
    - jump
    - hike
    - walk
    - fly
    He tags the bird with a tag.
    He views the view from his window.
    She covers the bed with a cover.
    She jumps from the high jump.
    To maintain the quiet, he quiets the children.
    She hikes up the mountain and it is a long hike.
    He take a long walk everyday to walk his dog.
    The fly flies away.
"""

sent1 = ["He views the view from his window.",
         "She jumps from the high jump.",
         "He takes a walk everyday to walk his dog.",
         "The fly flies away."]

sent2 = ["The cook cooks on the stove and bakes in the oven.",
         "She works on her work in the library.",
         "The man knocks on the door and the knocks were heard in the house."]

sent3 = ["Book the cooks who cook the books."]


def tagger(sentence):
    tagged = nltk.corpus.treebank.tagged_words()
    cfd_1 = nltk.ConditionalFreqDist(tagged)
    cfd_2 = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged)
    tagged = dict((word, tag) for (word, tag) in tagged)
    baseline_tagger = nltk.UnigramTagger(model=tagged)

    for sent_obj in sentence:
        sent = nltk.word_tokenize(sent_obj)
        print(baseline_tagger.tag(sent))
    print("\n")


"""
The tagger based on the WSJ corpus does not successfully tag all words 
in the input sentences. Some are labelled 'None' and others are incorrectly tagged. For instance,
"He tags the bird with a tag." is tagged as 
[('He', 'PRP'), ('tags', 'NNS'), ('the', 'DT'), ('bird', None), 
('with', 'IN'), ('a', 'DT'), ('tag', 'NN'), ('.', '.')]

In this sentence, both 'tags' and 'tag' are tagged as nouns, 
but 'tags' in this case is being used as a verb. In another sentence,

"She covers the bed with a cover."
both uses of the word 'cover' are tagged as verbs, even though the second occurrence is a noun.
"""


def main():
    """ Main function which is used as an interface """
    print("\n ********* Sentence 1 Tagger Results ********* \n")
    tagger(sent1)

    print("\n ********* Sentence 2 Tagger Results ********* \n")
    tagger(sent2)

    print("\n ********* Sentence 3 Tagger Results ********* \n")
    tagger(sent3)


if __name__ == '__main__':
    main()
