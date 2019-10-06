prlanguage = ['C++', 'Java', 'Python']
print("Enter a programming lanugage: ")
newlanguage = input()
if(newlanguage != 'C#' and newlanguage != 'C Sharp'):
    prlanguage.append(newlanguage)
    print(prlanguage[:])
else:
    print("C# is not allowed! Don't ask why")