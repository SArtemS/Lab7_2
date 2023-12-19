import os
import requests
import threading


def threadsForImages(url_list):
    threads = []
    for i in range(len(url_list)):
        url = url_list[i]
        file_name = f'1.Downloaded image {i+1}{os.path.splitext(url)[1]}'
        t = threading.Thread(target=downloadImage, args=[url, file_name])
        t.start()
        threads.append(t)

    for i in threads:
        t.join()


def downloadImage(url, file_name):
    image = requests.get(url)
    with open(file_name, 'wb') as f:
        f.write(image.content)
    print(f'Image downloaded and saved as {file_name}')
