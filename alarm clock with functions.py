import datetime
import webbrowser

def fetch_alarm() :
    alarmhour = int(input("hour :     "))

    i = 0

    if alarmhour>12 :
        print('we dont do that here.')
        webbrowser.open("https://www.youtube.com/watch?v=r39I7s-Wicc")
        exit()

    alarmMin = int(input("minute    : "))

    am_pm= str(input("am or pm :  "))

    ring_alarm(alarmhour,alarmMin,am_pm)


def ring_alarm(alarmhour,alarmMin,am_pm) :

    if am_pm == 'pm' or am_pm == 'Pm' or am_pm == 'PM' :

        alarmhour = alarmhour + 12    
        

        
    while(1 == 1) :
        

        if  alarmhour == datetime.datetime.now().hour and alarmMin == datetime.datetime.now().minute :
            print("wake up brother ")
            webbrowser.open("https://www.youtube.com/watch?v=8pulHiaB6H0")
            
            exit()    


fetch_alarm()

