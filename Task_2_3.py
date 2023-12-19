import os
import requests
from concurrent.futures import as_completed, ThreadPoolExecutor
from threading import Semaphore


def futuresForImages(url_list, n_jobs):
    semaphore = Semaphore(n_jobs)
    with ThreadPoolExecutor(max_workers=n_jobs) as executor:
        spawns = [
            executor.submit(downloadImage, url, url_list.index(url), semaphore)
            for url in url_list
        ]
    for spawn in as_completed(spawns):
        res = spawn.result()
        print(res)


def downloadImage(url, index, semaphore):
    with semaphore:
        image = requests.get(url)
        file_name = f'2.Downloaded image {index+1}{os.path.splitext(url)[1]}'
        with open(file_name, 'wb') as f:
            f.write(image.content)
        return (f'Image downloaded and saved as {file_name}')
