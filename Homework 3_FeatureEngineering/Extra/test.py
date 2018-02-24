import pandas as pd
import pickle

# d = pd.read_csv("data/spoilers/train.csv")
#
# list_set = set(d['page'])
# print(len(list_set))
#
#
# with open('movie_rating_test_dump.pickle','rb') as rating_file:
#     dump = pickle.load(rating_file)
#     train_rating = dump[0]
#     print(len(train_rating))

feature_list = []

feature_list.extend(['n_words', 'n_chars', 'toolong', 'allcaps',
                     'max_len', 'mean_len', 'bad_ratio',
                     'n_bad', 'capsratio', "n_nicks", "n_urls", "n_sentences",
                     "n_non_words", "idiot_regexp", "moron_regexp", "n_html", "strong_pos", "strong_neg", "weak_pos",
                     "weak_neg"])

print(feature_list)
