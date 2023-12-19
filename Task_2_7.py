import threading
import time

barrier = threading.Barrier(2, timeout=5)


def barrierForServer():
    time.sleep(2)
    print("The server is started")
    barrier.wait()
    print("Request received from client")


def barrierForClient():
    barrier.wait()
    print("The client sent a request to the server")


def clientRequest():
    serverThread = threading.Thread(target=barrierForServer)
    clientThread = threading.Thread(target=barrierForClient)

    serverThread.start()
    clientThread.start()

    serverThread.join()
    clientThread.join()
