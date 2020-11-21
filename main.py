import time
from datetime import datetime

hosts = "C:\Windows\System32\drivers\etc"
red = "127.0.0.1"

sites = ["youtube.com"]

while True:
    if datetime(datetime.now().year, datetime.now().month, datetime.now().day, 20) < datetime.now() < datetime(datetime.now().year, datetime.now().month, datetime.now().day, 21):
        print('Working')
        with open(hosts, 'r+') as file:
            content = file.read()
            for site in sites:
                if site in content:
                    pass
                else:
                    file.write(red + " " + site + "\n")
    else:
        with open(hosts, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(site in line for site in sites):
                    file.write(line)
            file.truncate()
        print('4 hours')
    time.sleep(4)
