import imdb
import pickle
import re
import pandas as pd
ia = imdb.IMDb()

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

zero_voting_count = {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}

error_analysis = {}
def find_rating(list_page):
    rating_dict = {}
    user_voting_dict = {}
    for movie in list_page:
        li = re.findall('[A-Z][^A-Z]*', movie)
        title = mearge(li)
        try:
            s_result = ia.search_movie(title)
            movie_id =  str(s_result[0].movieID)
            voting = ia.get(movieID=movie_id)
            rating = voting.get('data').get('demographics').get('imdb users').get('rating')
            user_voting_count = voting.get('data').get('number of votes')
            rating_dict[movie] = rating
            user_voting_dict[movie] = user_voting_count
        except:
            print("No movie id for this movieid = ", movie_id )
            error_analysis[movie_id] = movie
            rating_dict[movie] = 0
            user_voting_dict[movie] = zero_voting_count
    for id, movie in error_analysis.items():
        try:
            voting = ia.get_movie_vote_details(movieID=id)
            rating = voting.get('data').get('demographics').get('imdb users').get('rating')
            rating_dict[movie] = rating
            user_voting_count = voting.get('data').get('number of votes')
            user_voting_dict[movie] = user_voting_count
        except:
            print("No Movie id again for this movieid = ", id)
            rating_dict[movie] = 0
            user_voting_dict[movie] = user_voting_count
    return rating_dict,user_voting_dict

def rating_file_creation():
    filename = ['data/spoilers/train.csv','data/spoilers/test.csv']
    dump_file_rating = []
    dump_file_user_voting = []
    for file in filename:
        df = pd.read_csv(file)
        list_page = set(df['page'])
        rating,user_voting = find_rating(list_page)
        dump_file_rating.append(rating)
        dump_file_user_voting.append(user_voting)
    with open('movie_rating_test_dump.pickle', 'wb') as handle:
           pickle.dump(dump_file_rating, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('movie_user_voting_dump.pickle', 'wb') as handle:
           pickle.dump(dump_file_user_voting, handle, protocol=pickle.HIGHEST_PROTOCOL)


rating_file_creation()