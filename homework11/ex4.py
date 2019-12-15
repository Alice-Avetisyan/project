from multiprocessing import Process, Pipe
from random import choice


def transfer(words, connection):
    for i in range(len(words)):
        word = choice(words)
        connection.send(word)


def read(connection):
    while True:
        received_word = connection.recv()
        if received_word != "End":
            print("Received words: ", received_word)
        else:
            break


if __name__ == "__main__":

    words_list = ['I am a text', 'I am not very creative', 'I do not know what to write here', 'End']
    transfer_info, read_info = Pipe()

    times_to_repeat = 10
    while times_to_repeat >= 0:
        p1 = Process(target=transfer, args=(words_list, transfer_info))
        p2 = Process(target=read, args=(read_info,))

        p1.start()
        p1.join()

        p2.start()
        p2.join()

        times_to_repeat -= 1
