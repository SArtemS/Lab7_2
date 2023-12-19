import threading
import time


def checkEventStatus(event):
    time.sleep(2)
    event.set()


def eventOccurred(event):
    event.wait()
    print("Event occurred")


def eventDidNotOccurred(event):
    while not event.is_set():
        print("Event did not occurred")
        time.sleep(1)


def myEventSet():
    myEvent = threading.Event()

    firstEvent = threading.Thread(target=checkEventStatus, args=[myEvent])
    secondEvent = threading.Thread(target=eventOccurred, args=[myEvent])
    thirdEvent = threading.Thread(target=eventDidNotOccurred, args=[myEvent])

    firstEvent.start()
    secondEvent.start()
    thirdEvent.start()
