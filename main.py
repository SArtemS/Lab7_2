import random
import threading
import time
from Task_1_1 import showThreadNamesList
from Task_1_2 import threadsForImages
from Task_1_3 import threadsForHTTP
from Task_1_4 import FactorialThread
from Task_1_5 import quickSort
from Task_2_2 import BankThread
from Task_2_3 import futuresForImages
from Task_2_4 import futuresWriteAndRead
from Task_2_5 import myEventSet
from Task_2_6 import Queue
from Task_2_7 import clientRequest
from Task_2_8 import threadForSearchingFile


def pauseForShowcase(n=2):
    time.sleep(n)


if __name__ == '__main__':
    print("Task 1.1")
    showThreadNamesList(5)

    pauseForShowcase()

    print("\nTask 1.2")
    images_url_list = [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Image_created_with_a_mobile_phone.png/1280px-Image_created_with_a_mobile_phone.png",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/800px-Python-logo-notext.svg.png",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Chen_Hongshou%2C_leaf_album_painting.jpg/800px-Chen_Hongshou%2C_leaf_album_painting.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Visual_Studio_Code_1.35_icon.svg/1024px-Visual_Studio_Code_1.35_icon.svg.png"
    ]
    threadsForImages(images_url_list)

    pauseForShowcase()

    print("\nTask 1.3")
    http_request_url_list = [
        "https://ya.ru", "https://www.google.com",
        "https://moodle.herzen.spb.ru", "https://www.python.org/"
    ]
    threadsForHTTP(http_request_url_list)

    pauseForShowcase()

    print("\nTask 1.4")
    fact = FactorialThread(6)
    fact.factorialTwoThreads()
    print(f'Factorial {fact._n} = {fact._value}')

    pauseForShowcase()

    print("\nTask 1.5")
    lstToSort = [random.randint(0, 200) for i in range(20)]
    print(f'List: {lstToSort}')
    quickSort(lstToSort)
    print(f'Sorted List: {lstToSort}')

    pauseForShowcase()

    print("\nTask 2.1 on GitHub:\nhttps://github.com/SArtemS/Lab7_1")
    # https://github.com/SArtemS/Lab7_1

    pauseForShowcase()

    print("\nTask 2.2")
    YourAccount = BankThread(20000)
    threads = []
    for i in range(4):
        rnd = random.random()
        if rnd < 0.5:
            t = threading.Thread(
                target=YourAccount.deposit(random.randint(0, 30000)))
        else:
            t = threading.Thread(
                target=YourAccount.withdraw(random.randint(0, 30000)))
        t.start()
        threads.append(t)
        pauseForShowcase(1)
    for i in threads:
        t.join()

    pauseForShowcase()

    print("\nTask 2.3")
    images_url_list_2 = [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Python_logo_1990s.svg/1920px-Python_logo_1990s.svg.png",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Treblecsharp5.svg/1024px-Treblecsharp5.svg.png",
        "https://upload.wikimedia.org/wikipedia/ru/0/0f/Pygame_logo.png",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Android_2023_3D_logo_and_wordmark.svg/1920px-Android_2023_3D_logo_and_wordmark.svg.png"
    ]
    futuresForImages(images_url_list_2, 2)

    pauseForShowcase()

    print("\nTask 2.4")
    futuresWriteAndRead("Future File.txt", "That's my file!")

    pauseForShowcase()

    print("\nTask 2.5")
    myEventSet()

    pauseForShowcase(5)

    print("\nTask 2.6")
    myQueue = Queue()
    threads = []
    for i in range(6):
        rnd = random.random()
        if rnd < 0.5:
            t = threading.Thread(target=myQueue.add(random.randint(0, 30000)))
        else:
            t = threading.Thread(
                target=myQueue.remove(random.randint(0, 30000)))
        t.start()
        threads.append(t)
    for i in threads:
        t.join()

    pauseForShowcase()

    print("\nTask 2.7")
    clientRequest()

    pauseForShowcase()

    print("\nTask 2.8")
    threadForSearchingFile()
