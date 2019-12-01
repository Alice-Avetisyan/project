class Person:
    def __init__(self, theName, theHeight, theSex):
        self.name = theName
        self.height = theHeight
        self.sex = theSex

    def isTall(self, threshold):
        if self.height >= threshold:
            print("You are allowed on the ride")
        else:
            print("You are to short to be allowed on the ride")

    def isSex(self):
        if self.sex == 'Female' or self.sex == 'female' or self.sex == 'f':
            print("Women's dressing room is on the right")
        elif self.sex == 'Male' or self.sex == 'male' or self.sex == 'm':
            print("Men's dressing room is on the right")
        else:
            print("What are you?")

    def showPerson(self):
        print("Name: {0}; Height: {1}; Sex {2}".format(self.name, self.height, self.sex))


woman = Person('Anna', 155, 'female')
man = Person('Robert', 178, 'male')
print("---------------Person info---------------")
print("Person one: ", woman.showPerson())
print("Person two: ", man.showPerson())
print("---------------Tall enough---------------")
woman.isTall(160)
man.isTall(160)
print("-----------Which gender are you-----------")
woman.isSex()
