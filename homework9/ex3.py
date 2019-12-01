class Ticket:
    """This class contains information about tickets"""

    def __init__(self, theFrLocation, theToLocation, theTranspType, theDurationMnt, theArrivalTime, thePassenger):
        self.from_location = theFrLocation
        self.to_location = theToLocation
        self.transport_type = theTranspType
        self.duration_minutes = theDurationMnt
        self.arrival_time = theArrivalTime
        self.passenger = thePassenger

    #  set from/to
    def setLocation(self,SetFromLocation, SetToLocation):
        self.set_from_location = SetFromLocation
        self.set_to_location = SetToLocation
        print("Changing locations (from/to)")
        self.from_location = self.set_from_location
        self.to_location = self.set_to_location

    #  change transport type
    def transportType(self,changedTransportType):
        self.changed_transport_type = changedTransportType
        self.transport_type = self.changed_transport_type

    #  increase duration by some number
    def increaseDuration(self, changedDuration):
        self.changed_duration = changedDuration
        self.duration_minutes = self.changed_duration
    #  set passenger
    def setPassenger(self, theSetPassenger):
        self.set_passenger = theSetPassenger
        self.passenger = self.set_passenger

    def showTicket(self):
        print("Traveling from {0} location to {1} location; Transport type {2}; Duration of the travel in minutes {3}; "
              "Arrival time: {4}; Passanger name {5}".format(self.from_location, self.to_location, self.transport_type,
                                                             self.duration_minutes, self.arrival_time, self.passenger))


ticket1 = Ticket('Amsterdam', 'New_York', 'Train', 180, '3pm', 'Norman')
ticket2 = Ticket('Moskow', 'Erevan', 'Airplane', 120, '9am', 'Franklin')
print("---------------Ticket info---------------")
ticket1.showTicket()
ticket2.showTicket()

print("-------------Setting location-------------")
ticket2.setLocation('Moskow', 'Madrid')
ticket2.showTicket()
print("----------Changing transport type----------")
ticket1.transportType('Car')
ticket1.showTicket()
print("----------Increasing duration----------")
ticket1.increaseDuration(200)
ticket1.showTicket()
print("----------Setting passenger----------")
ticket2.setPassenger('Anna')

ticket1.showTicket()
ticket2.showTicket()


