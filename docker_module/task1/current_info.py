import datetime
from time import sleep

while True:
    now = datetime.datetime.now()
    print(now.strftime("%d-%m-%Y %H:%M:%S"))
    sleep(1)


