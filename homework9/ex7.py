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
        print("Wolf Class: ", self.wolfClass)


class Bear(Animal):
    """This class contains information about a bear and is a derived class"""

    def __init__(self, theAnimType, theEatingHab, isHibernating):
        super(Bear, self).__init__(theAnimType, theEatingHab)
        self.is_hibernating = isHibernating

    def showAnimal(self):
        super(Bear, self).showAnimal()
        print("Hibernating: ", self.is_hibernating)


print("---------------Wolf---------------")
wolf = Wolf('Wolf', 'Carnivore', 'Omega')
wolf.showAnimal()
print("---------------Bear---------------")
bear = Bear('Bear', 'Omnivore', 'No')
bear.showAnimal()
