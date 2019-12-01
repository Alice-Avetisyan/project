class Shop:
    """This class contains information about a shop"""
    def __init__(self, theEmplNames, theProdNames, thePrices, theOwner, theIncome):
        self.employee_names = theEmplNames
        self.product_names = theProdNames
        self.prices = thePrices
        self.owner = theOwner
        self.income = theIncome

    #  add employee
    def addEmployee(self, addEmpName):
        self.add_employee_name = addEmpName
        self.employee_names.append(self.add_employee_name)

    #  remove employee
    def removeEmployee(self, removeEmpName):
        self.remove_employee_name = removeEmpName
        self.employee_names.pop(self.remove_employee_name)

    #  add products
    def addProduct(self, addPrdName, addPrdPrice):
        self.add_product_name = addPrdName
        self.product_names.append(self.add_product_name)

        self.add_product_price = addPrdPrice
        self.prices.append(self.add_product_price)

    #  find product by name
    def findProduct(self, prodName):
        self.find_product_name = prodName
        for product in self.product_names:
            if self.find_product_name == product:
                print("We have that product")
                break
            else:
                print("We do not have that product")

    #  find the cheapest product (than some specific value)
    def findCheapestProd(self, theThreshold):
        self.threshold = theThreshold
        for price in self.prices:
            if price < self.threshold:
                print("We have a cheap product", price)
            else:
                continue
                print("We don't have cheaper than {0} threshold".format(self.threshold))
    #  change owner
    def changeOwner(self, changedOwnerName):
        self.changed_owner_name = changedOwnerName
        self.owner = self.changed_owner_name

    #  increase income
    def increaseIncome(self, theIncrease):
        self.increase_income = theIncrease
        self.income += self.increase_income


employees = ['Anna', 'Robert', 'Lisa', 'Brian']
products = ['Cheese', 'Meat', 'Milk']
prices = [500, 100, 150]
owner = 'Frank'
income = 500000

print("----------------Employee info----------------")
shop = Shop(employees, products, prices, owner, income)
print(shop.employee_names)

print("----------------Adding employee----------------")
shop.addEmployee('Mia')
print(shop.employee_names)

print("----------------Adding product----------------")
shop.addProduct('Juice', 50)
print(shop.product_names)
print(shop.prices)
print("----------------Finding product----------------")
shop.findProduct('Cheese')
print("----------Finding the cheapest product----------")
shop.findCheapestProd(100)
print("---------------Changing the owner---------------")
shop.changeOwner('Arnold')
print(shop.owner)
print("-------------Increasing the income-------------")
shop.increaseIncome(200)
