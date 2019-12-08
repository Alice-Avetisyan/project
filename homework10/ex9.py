from multiprocessing import Process
country_list = {'France': -24, 'Armenia': 3, 'Italy': 2, 'Taiwan': 10, 'Romania': -2}


def increment(country):
    print("Increment(T or I)")
    keys = list(country.keys())
    for key in keys:
        if key[0] == 'T' or key[0] == 'I':
            country[key] += 10
    for name in country.items():
        print(name)


def subtract(country):
    print("Subtract(A or R)")
    keys = list(country.keys())
    for key in keys:
        if key[0] == 'A' or key[0] == 'R':
            country[key] -= 5
    for name in country.items():
        print(name)


if __name__ == '__main__':
    p1 = Process(target=increment, args=(country_list, ))
    p1.start()
    p1.join()

    p2 = Process(target=subtract, args=(country_list, ))
    p2.start()
    p2.join()

    print("Processes are complete")



