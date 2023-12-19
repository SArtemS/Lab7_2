from threading import RLock


class Queue():

    def __init__(self):
        self._queue = []
        self._RLock = RLock()

    def add(self, object):
        with self._RLock:
            self._queue.append(object)
            print(f'{object} added!\nYour queue is: {self._queue}\n')

    def remove(self, object):
        with self._RLock:
            if len(self._queue) != 0:
                print(
                    f'{self._queue.pop(0)} removed!\nYour queue is: {self._queue}\n'
                )
            else:
                print("Your queue is empty!\n")
