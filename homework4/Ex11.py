import re
string = 'A boring string'
rexp = re.search('boring',string)
if rexp:
    print("Woohoo! Found it!")
else:
    print("We ain't found... nothing, we found nothing")