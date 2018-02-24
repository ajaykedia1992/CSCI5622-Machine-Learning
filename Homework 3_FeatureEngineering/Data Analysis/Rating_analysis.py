from matplotlib import pyplot as plt

kTARGET_FIELD = 'spoiler'
kRATING_FIELD = 'rating'
kPAGE_FIELD = 'page'
import pickle
with open("train.pickle", 'rb') as fifty_f:
    dfTrain = pickle.load(fifty_f)

with open('movie_rating_test_dump.pickle', 'rb') as rating_file:
    dump = pickle.load(rating_file)
    train_rating = dump[0]
    page = dfTrain[kPAGE_FIELD]
    rating_list = []
    for p in page:
        if p in train_rating:
            rating_list.append(train_rating[p])


dfTrain[kRATING_FIELD] = rating_list
spoiler_list = dfTrain.loc[dfTrain[kTARGET_FIELD] == 1]
non_spoiler_list = dfTrain.loc[dfTrain[kTARGET_FIELD] == 0]


page_group_spoiler = spoiler_list.groupby(kRATING_FIELD).size().sort_values(ascending=False)
page_group_nonspoiler = non_spoiler_list.groupby(kRATING_FIELD).size().sort_values(ascending=False)


fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.scatter(page_group_spoiler.index, page_group_spoiler.values, s=10, c='b', marker="s", label='spoiler')
ax1.scatter(page_group_nonspoiler.index, page_group_nonspoiler.values, s=10, c='r', marker="o", label='non-spoiler')
plt.xlabel('Rating')
plt.ylabel('count of pages')
plt.legend(loc='upper right')
plt.title('Rating : Spoiler and non-spoiler Analysis')
plt.show()

# plt.xticks(rotation='vertical')
# l1, = plt.plot(page_group_spoiler.values, label='Spoiler', marker='.', color = 'black')
# l2, = plt.plot(page_group_spoiler[page_group_nonspoiler.index], label='Non Spoiler', marker='o')
# plt.legend(handles=[l1, l2])
# plt.tight_layout()
# plt.title('Page : Top Spoiler Pages')
# plt.show()
#
# plt.xticks(rotation='vertical')
# l1, = plt.plot(page_group_nonspoiler.values, label='Non Spoiler', marker='.')
# l2, = plt.plot(page_group_nonspoiler[page_group_spoiler.index], label='Spoiler', marker='o', color = 'black')
# plt.legend(handles=[l1, l2])
# plt.title('Page : Top Non Spoiler distribution')
# plt.show()