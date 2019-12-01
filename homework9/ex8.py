class Smartphone:
    """This class contains information about a smartphone"""

    def __init__(self, thePhoneName, thePrice, thePhoneID):
        self.phone_name = thePhoneName
        self._price = thePrice
        self._ID = thePhoneID  # self.__ID -> AttributeError: 'Smartphone' object has no attribute '_ID'

    def showInfo(self):
        print("Phone name: {0}; Phone price: {1}; Phone ID: {2}".format(self.phone_name, self._price, self._ID))


smartphone = Smartphone('Samsung', 100, 'K2840')  # the ID is a private member
smartphone.showInfo()
