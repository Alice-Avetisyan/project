person1 = {'Avengers', 'Spider_man', 'Toy_Story2', 'Joker', 'Get_Out'}
person2 = {'Joker', 'Lion_King', 'IT', 'A_Quite_Place', 'Toy_Story2'}

print("-----------------------------------------------------------")
print("Watched at least by one of them: ", person1 & person2)
print("-----------------------------------------------------------")
print("Watched by 1-st and not watched by 2-nd: ", person1 - person2)