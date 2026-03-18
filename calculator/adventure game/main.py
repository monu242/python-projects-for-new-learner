#adventure game :-
import time


print("Welcome to the adventure game window 😈 ...")

print("x-------------x--------------x------------x")

name = input("Enter the name through which you want to enter the game : ")

print("Nice",name,"thanks for entering the game")
print("Let's begin 😀")

print("x-------------x--------------x------------x")

answer_user = input("You were travelling in jungle but your monster truck fuel is finished and now you meet the dead end if you will go straight you will die 😰..But their is a twist you have two options Left or Right \nChoose one of these 🧠 :  ").lower()
print("x-------------x--------------x------------x")
print(" So you choose",answer_user,"Interesting choice 😬. lets see your fate ")
print("x-------------x--------------x------------x")

if answer_user == "left":
    options = input("after walking through this path .. you reach a point where you see two people waiting there and there is only river  after them" \
    "\nthe person standing on right is looking normal and just have car  keys..\nthe person standing on left is doctor looking old but athletic.\nChoose person on right or left : ").lower()
    if options == "right":
        print("You are dead because car can'not take you to your destination.")
    elif options == "left":
        print("You are intteligent you have choose doctor so he can treat you and he is athletic so he will take you to your destination and you are safe")
    else:
        print("you choosed wrong option you die!")


if answer_user == "right":
    options_2 = input("you reach a place where everything is dark and you can't see anything and you are getting panicked but with the help of your blurred vision you are seeing two ways either you can go back and choose left side or continue walking..\nChoose back to the start or continue : ").lower()

    if options_2 == "back":
        print("You are dead while reaching at the starting point you getted cought into pit hole and wild rats eated you")
    elif options_2 == "continue":
        paths = input("so coming this way you reached a point where so see that there is a little computer there ... it shows two options either continue this adventure and win '2million$' or get the keys on the table and go home : ").lower()
        if paths == "continue the adventure":
            choose_the_impossible = input ("After coming in this way you see that your wife is sitting there with a person holding a knife on her neck and 2millon$ bag  in other room.\nNotification come to your phone and it says either choose your wife or money.:")
            if choose_the_impossible == "wife":
                 print("you  are good human being and good husband too ")
                 print("wait for 10 seconds")
                 time.sleep(10)
                 print("as you have choose to save your wife you have won 10 millions $ ")
            elif choose_the_impossible == "2million$":
                print("you have won 2million$")
                print("take the keys from the table in the left side of your wife dead body")
                print("he starts to walk to reach the table")
                time.sleep(5)
                print("his wife kills him by the knife which was in her neck")
            else:
                print("you choose wrong thing this game is ended ")

print("x-------------x--------------x------------x")
print("Thanks for playing this thrilling game ")
#done and dusted



