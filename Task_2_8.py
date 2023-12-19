import os
from concurrent.futures import as_completed, ThreadPoolExecutor


def searchFileInDirecory(index, searched_file, dir):
    for root, _, files in os.walk(dir):
        if searched_file in files:
            return (index, os.path.join(root, searched_file))


def threadForSearchingFile(n_jobs=5,
                           file_name="my_hidden_file.txt",
                           dir=os.getcwd()):
    with ThreadPoolExecutor(max_workers=n_jobs) as executor:
        spawns = [
            executor.submit(searchFileInDirecory, i, file_name, dir)
            for i in range(n_jobs)
        ]
    for spawn in as_completed(spawns):
        res = spawn.result()
        if res:
            print(f'File found with {res[0]} Thread, path: {res[1]} ')
            executor.shutdown()
            break
