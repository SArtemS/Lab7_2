import threading


class FactorialThread(threading.Thread):

    def __init__(self, n):
        super().__init__()
        self._n = n
        self._value = 1

    def factorial(self, n_start, n_end):
        fact = 1
        for i in range(n_start, n_end):
            fact *= i
        self._value *= fact

    def factorialTwoThreads(self):
        if (self._n <= 1): return
        threads = []
        a = [1, self._n // 2 + 1]
        b = [self._n // 2 + 1, self._n]
        for i in range(2):
            t = threading.Thread(target=self.factorial, args=[a[i], b[i]])
            t.start()
            threads.append(t)

        for i in threads:
            t.join()

    def get(self):
        return self._value
