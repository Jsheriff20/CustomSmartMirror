import time

def getHoursAndMins():
    while True:
        formatTime = time.strftime("%H:%M")
        time.sleep(1)
        print(str(formatTime))

        if(str(formatTime) == "00:00"):
            #update the date
            print()


def getSecs():
    while True:
        formatTime = time.strftime("%S")
        time.sleep(1)
        print(str(formatTime))

        if(str(formatTime) == "00"):
            #update the hours and mins
            print()



def getDate():
    while True:
        Date = time.strftime("%A %d %B")
        time.sleep(1)
        print(str(Date))


getDate()