class Building:
    """This class contains information about a building"""

    def __init__(self, theAddress, theNumberofFloors, theNumberofRoom):
        self.address = theAddress
        self.floors_number = theNumberofFloors
        self.room_number = theNumberofRoom


class Hotel(Building):
    """This class contains information about a hotel and is a derived class"""

    def __init__(self, Address, fl_num, room_num, thePrice, theBookedRoom):
        super(Hotel, self).__init__(Address, fl_num, room_num)
        self.price = thePrice
        self.booked_room = theBookedRoom

    def showHotelInfo(self):
        print("Address: {0}; Number of the floor: {1}; Room number: {2}; Price: {3}; Booked: {4}"
              .format(self.address, self.floors_number, self.room_number, self.price, self.booked_room))

    def Bookig(self):
        if self.room_number == -1 or self.floors_number == -1:
            print("Something went wrong")
        else:
            print("The hotel has {0} rooms and {1} floors".format(self.room_number, self.floors_number))
            print("Would you like to book a room? (Yes or No)")

            self.choice = input()
            if self.choice == 'Yes' or self.choice == 'yes' or self.choice == 'y':
                self.booked_room = 'Booked'
                print("Enjoy your stay")
            else:
                print("Have a nice day")

    @property
    def floors_number(self):
        return self._floors_number

    @floors_number.setter
    def floors_number(self, value):
        if value <= 12:
            self._floors_number = value
        else:
            self._floors_number = -1
            print("Invalid input: ", value)

    @property
    def room_number(self):
        return self._room_number

    @room_number.setter
    def room_number(self, value):
        if value <= 26:
            self._room_number = value
        else:
            self._room_number = -1
            print("Invalid input: ", value)


hotel = Hotel("LinkolnPark", 12, 26, 15, 'Not/Booked')
print("---------------Hotel info---------------")
hotel.showHotelInfo()

hotel_room = Hotel("LinkolnPark", 13, 6, 15, 'NotBooked')
print("-------------Booking a room-------------")
hotel_room.Bookig()
hotel_room.showHotelInfo()
