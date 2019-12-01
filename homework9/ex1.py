class Book:
    """This class contains information about a book"""
    def __init__(self, theAuthor, theOwner, thePages, thePrice, theCurPage):
        self.author = theAuthor
        self.owner = theOwner
        self.pages = thePages
        self.price = thePrice
        self.crnt_page = theCurPage

    def changeOwner(self, theOwnerName):
        self.ownerName = theOwnerName
        print("You have changed the onwer's name successfully")
        self.owner = self.ownerName

    def increasePrice(self, theIncdPrice):
        self.incdPrice = theIncdPrice
        print("The price of the book has been increased")
        self.price += self.incdPrice

    def changeCrntPage(self, theChangeCrntPage):
        self.chageCrntPage = theChangeCrntPage
        print("The current page has been changed")
        self.crnt_page = self.chageCrntPage

    def __str__(self):
        return "Author's name: " + self.author + "; Owner's name: " + self.owner + "; Pages: " + str(self.pages) + "; Price: " + str(self.price) + "; Current Page: " + str(self.crnt_page)

    def __repr__(self):
        return __str__


book1 = Book('Ray_Bradbury', 'Robert', 150, 25, 15)
book2 = Book('William_Shakespeare', 'Lisa', 250, 50, 245)

print("---------------Book info---------------")
print("Book one: ", book1)
print("Book two: ", book2)

print("-----Changing the book's owner-----")
book1.changeOwner("Anna")
print("Book one(changed owner): ", book1)

print("--------Changing the book's price--------")
book2.increasePrice(15)
print("Book two(increased price): ", book2)

print("-----Changing the book's current page-----")
book2.changeCrntPage(250)
print("Book two(current page): ", book2)
