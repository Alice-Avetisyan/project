def greater_than(action, number):
    """Checking if the numbers is greater than 10"""
    if number >= 10:
        print("Your entered number is greater than 40: ")
        print("Executing the action: ", action(number))
    else:
        print("!!!! Your entered number is smaller than 40: ", number)


print("Please enter a number: ")
num_inp = int(input())  # num>20 or num<20
print("Please enter another number: ")
pow_inp = int(input())  # number for the lambda


greater_than(lambda x: x ** pow_inp, num_inp)
