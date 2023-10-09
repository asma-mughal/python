movie ={
    'title':'Life of Brain',
    'year': 9988,
    'cast': ['Terry', 'Eric', "Georage"]

}
print(movie['title'])
print(movie.get('title'))
print(movie.get('budget', 'Not found'))
movie['title'] = "The Holy Grail"
print(movie)
movie['budget'] = "New budget"
print(movie)
movie.update({
    'ratings': 8,
    'Famous':True

})
print(movie)
#del movie['year']
year = movie.pop('year')
print(movie)
print(len(movie))
print(movie.keys())
print(movie.values())
print(movie.items())
for key, value in movie.items():
    print(key, value)