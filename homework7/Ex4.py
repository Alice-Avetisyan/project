hotel = {'room1': {'room_num': 1, 'room_state': 'booked', 'room_type': 'econom'},
         'room2': {'room_num': 2, 'room_state': 'not/b', 'room_type': 'econom'},
         'room3': {'room_num': 3, 'room_state': 'not/b', 'room_type': 'lux'},
         'room4': {'room_num': 4, 'room_state': 'booked', 'room_type': 'business'}}

def booked_rooms(hotel):
    keys = list(hotel.keys())
    count = 0
    for key in keys:
        if hotel[key]['room_state'] == 'booked':
            count += 1
    print("There is/are {0} booked room/s".format(count))

def nbooked_lrooms(hotel):
    keys = list(hotel.keys())
    count = 0
    for key in keys:
        if hotel[key]['room_state'] == 'not/b' and hotel[key]['room_type'] == 'lux':
            count += 1
    print("There is/are {0} not booked lux room/s".format(count))

def check_room_type(hotel, room_type):
    keys = list(hotel.keys())
    count = 0
    for key in keys:
        if hotel[key]['room_state'] == 'not/b' and hotel[key]['room_type'] == room_type:
            count += 1
    print("There is/are {0} {1} room/s".format(count, room_type))

new_list = []
keys = list(hotel.keys())
for key in keys:
    if hotel[key]['room_type'] == 'econom':
        new_list.append(hotel[key])

print("Rooms with econom type/s is/are: ", new_list)

booked_rooms(hotel)
nbooked_lrooms(hotel)  # not flexible
check_room_type(hotel, 'lux')  # the same thing as the one above but more flexible
