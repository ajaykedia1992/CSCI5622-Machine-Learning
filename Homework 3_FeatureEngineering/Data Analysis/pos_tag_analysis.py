import pandas as pd
from matplotlib import pyplot as plt
import nltk

kTARGET_FIELD = 'spoiler'
kTEXT_FIELD = 'sentence'

all_possible_tags = ['WRB', 'WP$', 'WP', 'WDT', 'VBZ', 'VBP', 'VBN', 'VBG', 'VBD', 'VB', 'UH', 'TO', 'SYM', 'RP', 'RBS', 'RBR', 'RB', 'PRP$', 'PRP', 'POS', 'PDT', 'NNS', 'NNPS', 'NNP', 'NN', 'MD', 'LS', 'JJS', 'JJR', 'JJ', 'IN', 'FW', 'EX', 'DT', 'CD', 'CC']
all_possible_tags = sorted(all_possible_tags)
print(all_possible_tags)
spoiler_pos_dict = {}
non_spoiler_pos_dict = {}

for tag in all_possible_tags:
    spoiler_pos_dict[tag] = 0
    non_spoiler_pos_dict[tag] = 0

dfTrain = pd.read_csv("data/spoilers/train.csv")

for index,row in dfTrain.iterrows():
    sentence = row[kTEXT_FIELD]
    tags = nltk.pos_tag(sentence)

    spoiler = row[kTARGET_FIELD]
    d = None
    if spoiler:
        d = spoiler_pos_dict
    else:
        d = non_spoiler_pos_dict

    for tup in tags:
        if tup[-1] in d.keys():
            d[tup[-1]] += 1
        else:
            pass

print(spoiler_pos_dict)
print(non_spoiler_pos_dict)

D = spoiler_pos_dict

x = range(len(D))
y = list(D.values())
z = list(D.keys())
plt.title('Spoiler : POS word Count')
plt.figure(figsize=(6,15))
plt.bar(x, y, align='center')
plt.xlabel('Part of Speech Tag')
plt.ylabel('Count of words')
plt.xticks(x, z)
plt.show()



D = non_spoiler_pos_dict
x = range(len(D))
y = list(D.values())
z = list(D.keys())
plt.title('Non-Spoiler : POS word Count')
plt.figure(figsize=(6,15))
plt.bar(x, y, align='center')
plt.xlabel('Part of Speech Tag')
plt.ylabel('Count of words')
plt.xticks(x, z)

plt.show()
