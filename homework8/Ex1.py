movies = ['Avengers', 'Terminator', 'RushHour', 'IT']

addMovie = lambda x: movies.append(x)
searchMovie = list(filter(lambda x: x == 'Avengers' or x == 'IT', movies))

addMovie('SpiderMan')
print("The list contains: ", movies)

print(searchMovie)
