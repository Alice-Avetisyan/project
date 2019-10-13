print("Please input thy string: ")
instring = input()
print("The length of the string is: ", len(instring))
if len(instring)%2==0:
    print("start to half: ", instring[:len(instring) // 2])
else:
    print("half to the end: ", instring[len(instring) // 2:])
