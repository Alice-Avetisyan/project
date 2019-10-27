hotel = {'visitor1': {'name': 'Anna', 'country': 'Germany'},
         'visitor2': {'name': 'Chris', 'country': 'USA'},
         'visitor3': {'name': 'Jill', 'country': 'Britain'}}
for i in range(2):
    print("Enter the visitor's name")
    name = input()
    print("Enter the country's name")
    country = input()
    key = 'visitor' + str(len(hotel) + 1)
    hotel[key] = {'name': name, 'country': country}

print(len(hotel))
for key in hotel.keys():
    print(hotel[key]['name'])
    print(hotel[key]['country'])



