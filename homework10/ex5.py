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

    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, value):
        if value == 'female' or value == 'male':
            self._sex = value
        else:
            self._sex = -1
            print("Error", value)

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value < 0:
            self._height = value
            print("o_o -_- o_o -_-...o_o")
        elif value > 200:
            self._height = value
            print("(while looking up) 0_0 -_- 0_0 -_-...0_0")
        else:
            self._height = value


woman = Person('Anna', -1, 'female')
man = Person('Robert', 228, 'male')
print("---------------Person info---------------")
print("Person one: ", woman.showPerson())
print("Person two: ", man.showPerson())
print("---------------Tall enough---------------")
woman.isTall(160)
man.isTall(160)
print("-----------Which gender are you-----------")
woman.isSex()
