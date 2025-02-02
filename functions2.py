# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#1
def is_IMDB_above_5_5(movie):
    for i in range(len(movies)):
        if movies[i]["name"]==movie:
            if movies[i]["imdb"]>5.5:
                return True
            else:
                return False
print(is_IMDB_above_5_5("We Two"))
print(is_IMDB_above_5_5("Exam"))

#2
def is_list_IMDB_above_5_5(movie):
    list_of_movies=[]
    for i in range(len(movie)):
        if movie[i]["imdb"]>5.5:
            list_of_movies.append(movie[i]["name"])
    return list_of_movies
print(is_list_IMDB_above_5_5(movies))

#3
def category_of_movies(category):
    list_of_movies=[]
    for i in range(len(movies)):
        if movies[i]["category"]==category:
            list_of_movies.append(movies[i]["name"])
    return list_of_movies
print(category_of_movies("Romance"))

#4
def average_IMDB_score(movie):
    count=0
    avg=0
    for i in range(len(movie)):
        avg=avg+movie[i]["imdb"]
        count=count+1
    return avg/count
print(average_IMDB_score(movies))

#5
def category_of_movies(category):
    avg=0
    count=0
    for i in range(len(movies)):
        if movies[i]["category"]==category:
            avg=avg+movies[i]["imdb"]
            count=count+1
    return avg/count
print(category_of_movies("Romance"))

