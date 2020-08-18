from pymongo import MongoClient

# mongodb connection
client = MongoClient('localhost', 27017)

db = client[ "tweet_database"] 
movie_collection = db['movie_collection']

s = movie_collection.find({})
extract_data = []

#extracting only imdbRating, Genre and Plot

for each in s:
    t = {}
    t['title'] = each['Title']
    t['rating'] = each['imdbRating']
    t['genre'] = each['Genre']
    t['plot'] = each['Plot']
    
    extract_data.append(t)
    
print(extract_data)
