import pandas as pd
from collections import Counter
import numpy as np
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from scipy.sparse import csr_matrix

dfTrain = pd.read_csv("data/spoilers/train.csv")
examples = dfTrain['sentence']
all_possible_tags = ['CC', 'CD', 'DT', 'EX', 'FW', 'IN', 'JJ', 'JJR', 'JJS', 'LS', 'MD', 'NN', 'NNP', 'NNPS',
                             'NNS', 'PDT', 'POS', 'PRP', 'PRP$', 'RB', 'RBR', 'RBS', 'RP', 'SYM', 'TO', 'UH', 'VB',
                             'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WDT', 'WP', 'WP$', 'WRB', 'PUNCT']

POSWordCountDict = Counter(all_possible_tags)
dict = {k: v for v, k in enumerate(all_possible_tags)}
X = np.zeros((len(examples), len(all_possible_tags)))
ii = 0
for sentence in examples:
    words = word_tokenize(sentence)
    words_and_pos_tags = pos_tag(words)
    for word_and_pos in words_and_pos_tags:
        tag = word_and_pos[1]
        if tag not in all_possible_tags:
            tag = 'PUNCT'
        X[ii, dict[tag]] += 1
    ii = ii + 1
print(X)