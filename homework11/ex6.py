import time
from multiprocessing import Pool

number_list = [5.5] * 10000


def multiply(number):
    return number * 5


if __name__ == "__main__":
    start_time = time.time()

    pool = Pool()
    new_list = list(pool.map(multiply, number_list))
    print(new_list)

    end_time = time.time()
    print(end_time-start_time)
