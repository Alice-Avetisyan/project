class Smartphone:
    """This class contains information about a smartphone"""

    def __init__(self, thePhoneName, thePrice, thePhoneID):
        self.phone_name = thePhoneName
        self._ID = thePhoneID  # self.__ID -> AttributeError: 'Smartphone' object has no attribute '_ID'
        self._price = thePrice

    def showInfo(self):
        try:
            print("Phone name: {0}; Phone price: {1}; Phone ID: {2}".format(self.phone_name, self._price, self._ID))
        except:
            print("Something went wrong")
        finally:
            print("Execution ended")


smartphone = Smartphone('Samsung', 100, 'K2840')  # the ID is a private member
smartphone.showInfo()
