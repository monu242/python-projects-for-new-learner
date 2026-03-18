#so this is the project for alarm clock where we can give input fro time and then 
#after the time will end it is gonna play the sound
from playsound3 import playsound
import time
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elapsed = 0
    
    print(CLEAR)
    while time_elapsed<seconds:
        time.sleep(1)
        time_elapsed += 1
        
        time_left = seconds - time_elapsed
        hours = time_left//3600
        minute_left = time_left//60
        seconds_left = time_left% 60


        print(f"{CLEAR_AND_RETURN}Alarm will sound in {hours:02d}:{minute_left:02d}:{seconds_left:02d}")
    playsound('https://assets.mixkit.co/active_storage/sfx/1005/1005.wav')
Hours = int(input("how many hours do you want  :  "))
minutes = int(input("how many minutes  do you  want  :  "))
seconds = int(input("how many seconds do you want :   "))   
Total_time = Hours*60*60+minutes*60+seconds
alarm(Total_time)








