class Movie:
    """This class contains information about a movie"""

    count = 0

    def __init__(self, theTitle, theDirector, theDuration, theActors, theRating):
        self.title = theTitle
        self.director = theDirector
        self.duration = theDuration
        self.actors = theActors
        self.rating = theRating
        Movie.count += 1  # static variable

    #  find if movie director name starts with specific symbol
    def startsWith(self, theSymbol):
        self.symbol = theSymbol
        if self.director[0] == self.symbol:
            print(self.director)
        else:
            print("No director's name starts with ", self.symbol)
    #  find if some person is an actor
    def isActor(self, theActorName):
        self.actorName = theActorName
        for actor in self.actors:
            if self.actorName == actor:
                print(actor)
                break
            else:
                print("We don't have an actor with that name")
    #  change rating
    def changeRating(self, theChangedRating):
        self.changedRatign = theChangedRating
        self.rating = self.changedRatign
        print("The rating has been changed")

    def showMovie(self):
        print("Movie name {0}; Director {1}; Duration {2}; Actor {3}; Rating {4}".
              format(self.title, self.director, self.duration, self.actors, self.rating))


actors1 = ['Sylvester_Stallone', 'Richard_Crenna', 'Brian_Dennehy']
actors2 = ['Mark_Hamill', 'Harrison_Ford', 'Carrie_Fisher']
actors3 = ['Chris_Pratt', 'Will_Ferrell', 'Elizabeth_Banks']

movie1 = Movie('First_Blood', 'Ted_Kotcheff', 2, actors1, 4.5)
movie2 = Movie('Star_Wars', 'Irvin_Kershner', 3, actors2, 4.8)
movie3 = Movie('Lego_Movie', 'Phil_Lord', 1, actors3, 4.6)
print("---------------Movie info---------------")
movie1.showMovie()
movie2.showMovie()
movie3.showMovie()
print("---------------Starts with---------------")
movie1.startsWith('T')
print("---------------Change rating---------------")
movie2.changeRating(5)
print("---------------Find actor---------------")
movie3.isActor('Chris_Pratt')

print("There are ", movie1.count, " movies")




