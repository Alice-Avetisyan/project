class Building:
    """This class contains information about a building"""

    def __init__(self, theAddress, theNumberofFloors, theNumberofRooms):
        self.address = theAddress
        self.floors_number = theNumberofFloors
        self.rooms_number = theNumberofRooms

class Hotel(Building):
    """This class contains information about a hotel and is a derived class"""

    def __init__(self, Address, fl_num, room_num, thePrice, theBookedRoom):
        super(Hotel, self).__init__(Address, fl_num, room_num)
        self.price = thePrice
        self.booked_rooms = theBookedRoom

    def showHotelInfo(self):
        print("Address: {0}; Number of floors: {1}; Number of rooms: {2}; Price: {3}; The number of booked rooms: {4}".format(self.address, self.floors_number, self.rooms_number, self.price, self.booked_rooms))

    def Bookig(self, theChoice):
        print("The hotel has {0} rooms and {1} booked rooms".format(self.rooms_number, self.booked_rooms))
        self.choice = theChoice
        print("Would you like to book a room? (Yes or No)")

        if self.choice == 'Yes' or self.choice == 'yes' or self.choice =='y':
            self.booked_rooms += 1
            print("The hotel has {0} rooms and {1} booked rooms".format(self.rooms_number, self.booked_rooms))
            print("Enjoy your stay")
        else:
            print("The hotel has {0} rooms and {1} booked rooms".format(self.rooms_number, self.booked_rooms))
            print("Have a nice day")

    def Bookig_test(self):
        print("The hotel has {0} rooms and {1} booked rooms".format(self.rooms_number, self.booked_rooms))
        print("Would you like to book a room? (Yes or No)")
        self.choice = input()
        if self.choice == 'Yes' or self.choice == 'yes' or self.choice =='y':
            self.booked_rooms += 1
            print("The hotel has {0} rooms and {1} booked rooms".format(self.rooms_number, self.booked_rooms))
            print("Enjoy your stay")
        else:
            print("The hotel has {0} rooms and {1} booked rooms".format(self.rooms_number, self.booked_rooms))
            print("Have a nice day")


hotel = Hotel("LinkolnPark", 12, 26, 15, 20)
print("---------------Hotel info---------------")
hotel.showHotelInfo()
print("-------------Booking a room-------------")
hotel.Bookig('Yes')
print("----------------------------------------")

print("----------Booking a room(test)----------")  # using an input inside of the classes method
hotel.Bookig_test()
