# Ex 9 => module 2
import room
print("Please enter the color of the apartment: ")
color = input()
print("Please enter the number of the rooms: ")
roomnum = int(input())
print("Please enter if you would like the apartment to be new (y|n): ")
inew = input()
if((color == room.color1 or color == room.color2) and (roomnum == room.rnumber1 or roomnum == room.rnumber2)):
    if(roomnum == room.rnumber1 and inew == room.new):
        print("We have a new apartment. The rooms are: ", color, ", the apartment has ", roomnum, " rooms and costs: ", room.cost*2)
    else:
        print("The apartment is old. The rooms are: ", color, ", the apartment has ", roomnum, " rooms and costs: ", room.cost)
else:
    print("Unfortunately we could not find an apartment suitable for you.")