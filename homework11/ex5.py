import multiprocessing
#from multiprocessing import Lock
#from threading import Lock


def add_ten(numbers, result, lock):
    for i in range(5000):
        for idx, n in enumerate(numbers):
            lock.acquired()
            result[idx] = n + 10
            lock.release()


def subtract_five(numbers, result, lock):
    for i in range(10000):
        for idx, n in enumerate(numbers):
            lock.acquired()
            result[idx] = n - 5
            lock.release()


if __name__ == "__main__":

    number_list = [2, 3, 5]
    result = multiprocessing.Array('i', 3)
    lock = multiprocessing.Lock()

    p1 = multiprocessing.Process(target=add_ten, args=(number_list, result, lock))
    p2 = multiprocessing.Process(target=subtract_five, args=(number_list, result, lock))

    p1.start()
    p1.join()

    p2.start()
    p2.join()

    print("Result: ", result[:])
