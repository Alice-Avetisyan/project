class Animal:
    """This class contains information about an animal"""

    def __init__(self, theAnimalType, theEatingHabit):
        self.animal_type = theAnimalType
        self.eating_habit = theEatingHabit

    def showAnimal(self):
        print("Animal Type: {0}; Eating Habit: {1}".format(self.animal_type, self.eating_habit))


class Wolf(Animal):
    """This class contains information about a wolf and is a derived class"""

    def __init__(self, theAnimType, theEatingHab, theWolfClass):
        super(Wolf, self).__init__(theAnimType, theEatingHab)
        self.wolfClass = theWolfClass

    def showAnimal(self):
        super(Wolf, self).showAnimal()
        if self.animal_type == 'Chicken':
            self.wolfClass = "I am a chicken, what class are you expecting?"
            print(self.animal_type, "Class: ", self.wolfClass)
        else:
            print(self.animal_type, "Class: ", self.wolfClass)

    @property
    def animal_type(self):
        return self._animal_type

    @animal_type.setter
    def animal_type(self, value):
        if value == 'Wolf':
            self._animal_type = value
        elif value == 'Chicken':
            self._animal_type = 'Chicken'
            print("I guess, I'm a chicken now... pck pck pck pck")
        else:
            self._animal_type = -1
            print("Invalid input: ", value)


class Bear(Animal):
    """This class contains information about a bear and is a derived class"""

    def __init__(self, theAnimType, theEatingHab, isHibernating):
        super(Bear, self).__init__(theAnimType, theEatingHab)
        self.is_hibernating = isHibernating

    def showAnimal(self):
        super(Bear, self).showAnimal()
        print("Hibernating: ", self.is_hibernating)

    @property
    def is_hibernating(self):
        return self._is_hibernating

    @is_hibernating.setter
    def is_hibernating(self, value):
        if value == 'No' or value == 'Yes':
            self._is_hibernating = value
        elif value == 'Party':
            self._is_hibernating = 'Party animal'
            print("Just one more glass")
        else:
            self._is_hibernating = -1
            print("Invalid input: ", value)


print("---------------Wolf---------------")
wolf = Wolf('Wolf', 'Carnivore', 'Omega')
wolf.showAnimal()
wolf_chick = Wolf('Chicken', 'Carnivore', 'Omega')
wolf_chick.showAnimal()
print("---------------Bear---------------")
bear = Bear('Bear', 'Omnivore', 'No')
bear.showAnimal()
bear_party = Bear('Bear', 'Omnivore', 'Party')
bear_party.showAnimal()
