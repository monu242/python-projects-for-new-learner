import random # for getting the random thing out of this 


top_of_range = input("Type a number for your range: ")

print("x-----------------x---------x--------------x------------x")

if top_of_range.isdigit():#.isdigit is for checking if the number is digit or not 
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please! type a number which is larger than 0 next time")
        quit()
else:
    print("please type a  positive number next time :-)")
    quit()

random_number = random.randint(0,top_of_range)
guess = 0

while True:
    guess += 1
    user_guess = input("Make a guess: ")
    
    if user_guess.isdigit():
        user_guess = int(user_guess)
    
    else:
        print("please type a number next time :-)")
        print("x----------------x--------------x---------------x--------------x")
        continue

    if user_guess == random_number:
        print("You got it correct")
        print(" x-----THE_END-------x")
        break
    elif user_guess>random_number:
        print("you were above the exceeding limit")
    else:
        print("you were below the number")    
    print("x---------------x---------------x----------------x-------------x")

print("Right answer got guessed in|",guess,"|chances.")




