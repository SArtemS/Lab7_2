from concurrent.futures import ThreadPoolExecutor
from threading import Semaphore


def futuresWriteAndRead(file_name, file_text):
    semaphore = Semaphore(1)
    with ThreadPoolExecutor() as executor:
        futureWrite = executor.submit(writeFile, file_name, file_text, semaphore)
        futureRead = executor.submit(readFile, file_name, semaphore)
        futureWrite.result()
        futureRead.result()


def writeFile(file_name, file_text, semaphore):
    with semaphore:
        with open(file_name, "w") as f:
            f.write(file_text)
            print(f'Your text is written to {file_name}')


def readFile(file_name, semaphore):
    with semaphore:
        with open(file_name, "r") as f:
            text = f.read()
            print(f'Text in {file_name}:\n{text}')
