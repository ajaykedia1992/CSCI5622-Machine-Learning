import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.base import BaseEstimator, TransformerMixin
import pickle
import imdb
from bs4 import BeautifulSoup
import requests
ia = imdb.IMDb()
str1 = 'https://www.imdb.com/title/tt'
#url = urllib.urlopen(str).read()
#bs = BeautifulSoup(r.text)
'''s_result = ia.search_movie('Break The Bank1985')

print(s_result)
# Print the long imdb canonical title and movieID of the results.
for item in s_result:
   print(item['long imdb canonical title'], item.movieID)'''

def mearge(li):
    str = ""
    art = ['in','a','the','and']
    #print(li)
    for i in range(len(li)):
        if li[i] != len(li)-1:
            if len(li[i]) > 1:
                #re.findall('\d+[a-z]', li[i])
                str += li[i] + ' '
            else:
                if (i+1) < len(li) and len(li[i+1])>1:
                    str += li[i] + ' '
                else:
                    str += li[i]
        else:
            str+= li[i]
    return str
#url = 'https://www.imdb.com/title/'
d = pd.read_csv("data/spoilers/train.csv")

list_set = set(d['page'])
#print(len(list_set))


pos = {}

episode_dict = {}
#for index,row in d.iterrows():
import pickle
def genre_find():
    error_list = {}
    for row in list_set:
        li = re.findall('[A-Z][^A-Z]*', row)
        title = mearge(li)
        try:
            s_result = ia.search_movie(title)
            print(title)
            movie_id = s_result[0].movieID
            print(s_result[0]['title'],movie_id)
            #str = str+ str(movie_id)+'/'
            print(str1+str(movie_id)+'/')
            url = requests.get(str1+str(movie_id)+'/')
            bs = BeautifulSoup(url.content,'html.parser')
            #print(list(bs.children))
            episode_tag = bs.find_all('span', {'class' : 'bp_secondary'})
            if len(episode_tag) == 0:
                episode_tag = bs.find_all('span',{'class' : 'bp_sub_heading'})
            if len(episode_tag) == 0:
                episode_dict[row] = 0
                continue
            cleanr = re.compile('\[?<.*?>]?')
            cleantext = re.sub(cleanr, '', str(episode_tag))
            episode = cleantext.split()
            episode_dict[row] = int(episode[0])
        except:
            print("No found for this one")
            episode_dict[row] = 0
            error_list[row] = movie_id
    
    for key, value in error_list.items():
        try:
            url = requests.get(str1 + str(movie_id) + '/')
            bs = BeautifulSoup(url.content, 'html.parser')
            # print(list(bs.children))
            episode_tag = bs.find_all('span', {'class': 'bp_secondary'})
            if len(episode_tag) == 0:
                episode_tag = bs.find_all('span', {'class': 'bp_sub_heading'})
            if len(episode_tag) == 0:
                episode_dict[row] = 0
                continue
            cleanr = re.compile('\[?<.*?>]?')
            cleantext = re.sub(cleanr, '', str(episode_tag))
            episode = cleantext.split()
            episode_dict[row] = int(episode[0])
        except:
            print("No found for this one again = ", key)
            episode_dict[row] = 0


    with open('episode_test_dump.pickle', 'wb') as handle:
        pickle.dump(episode_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)



genre_find()