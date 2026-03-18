#we are going to make a drink water reminder program
import time  # for time delay
from plyer import notification  #for notificationand used plyer bu installing it ..


while  True: #for infinit loop
    print("Drink some water now!")
   
    notification.notify(title = "Drink some water now", \
    message = "Please drink some water to stay hydrated")


    time.sleep(10)   # for making it reminder for one hour.