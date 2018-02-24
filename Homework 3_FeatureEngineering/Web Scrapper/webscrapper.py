from imdb import IMDb

ia = IMDb()

s = ia.search_movie('Deadpool')
dp = s[0]
# print(s)
# print(s1)
# print(s2)
# print(s3)
ia.update(dp)
print(dp.get('genre'))




#1431045