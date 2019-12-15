from multiprocessing import Process, Queue, Value


def add_three(number, queue):
    for i in range(1000):
        number.value = number.value + 3
    queue.put(number.value)


def printing(queue):
    while True:
        if not(queue.empty()):
            print(queue.get())
            break


if __name__ == "__main__":
    queue = Queue()
    variable = Value('i', 50)

    p1 = Process(target=add_three, args=(variable,  queue))
    p2 = Process(target=printing, args=(queue,))

    p1.start()
    p1.join()

    p2.start()
    p2.join()
