import requests
import threading


def threadsForHTTP(url_list):
    threads = []
    for i in range(len(url_list)):
        url = url_list[i]
        t = threading.Thread(target=http_request, args=[url])
        t.start()
        threads.append(t)

    for i in threads:
        t.join()


def http_request(url):
    r = requests.get(url)
    print(f'For {url}: {r}')
