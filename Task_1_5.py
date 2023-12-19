import threading


def partition(array, begin, end):
    pivot = begin
    for i in range(begin + 1, end + 1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot


def quickSort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1

    def _quickSort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)

        fromBeginThread = threading.Thread(target=_quickSort,
                                           args=[array, begin, pivot - 1])
        fromEndThread = threading.Thread(target=_quickSort,
                                         args=[array, pivot + 1, end])

        fromBeginThread.start()
        fromEndThread.start()

        fromBeginThread.join()
        fromEndThread.join()

    return _quickSort(array, begin, end)
