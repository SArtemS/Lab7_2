import threading


def showThreadNamesList(num_thread):
    threads = []
    for _ in range(num_thread):
        t = threading.Thread(target=showThreadName)
        t.start()
        threads.append(t)

    for i in threads:
        t.join()


def showThreadName():
    t_name = threading.current_thread()
    print("Thread's name:", t_name)
