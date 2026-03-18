print("Welcome to this amazing short quiz game")

print("_________________________________________")

user_input = input("if you want to play the game enter Yes or No : ")

print("_______________________________")


if (user_input.lower() == "yes"):
    print("You have entered the quiz! enjoy ::")
elif(user_input.lower() == "no"):
    
    print("Thanks")
    
    +quit()
score = 0

print("x--------------------x-------------------x------------------x")
print("Q - what is the capital of  india \n1.delhi\n2.chandigarh\n3.nepal\n4.Maharatra")

user_input_2 = int(input("Enter the correct option : "))

match user_input_2:
    case 1:
        print("Horray ! correct answer")
        score+= 1

    case 2:
        print("wrong answer")
    case 3:
        print("wrong answer")    
    case 4 :
        print("wrong answer")    


print("x--------------------x-------------------x------------------x")
print("Q - who is the inventor of  laws of motion \n1.newton \n2.Einstein \n3.thomas edison \n4.gallileo")

user_input_2 = int(input("Enter the correct option : "))

match user_input_2:
    case 1:
        print("Horray ! correct answer")
        score+= 1
    case 2:
        print("wrong answer")
    case 3:
        print("wrong answer")    
    case 4 :
        print("wrong answer")

print("x--------------------x-------------------x------------------x")
print("Q - what is the 2 divide by 4 \n1.0.5 \n2.2 \n3.5 \n4.3")

user_input_2 = int(input("Enter the correct option : "))

match user_input_2:
    case 1:
        print("Horray ! correct answer")
        score+= 1
    case 2:
        print("wrong answer")
        
    case 3:
        print("wrong answer")    
    case 4 :
        print("wrong answer")

print("x--------------------x-------------------x------------------x")

print("Q - what is the  value of 1 divide by infinity \n1.0 \n2.1 \n3.4\n4.10")

user_input_2 = int(input("Enter the correct option : "))

match user_input_2:
    case 1:
        print("Horray ! correct answer")
        score+= 1
    case 2:
        print("wrong answer")
    case 3:
        print("wrong answer")    
    case 4 :
        print("wrong answer")

print("x--------------------x-------------------x------------------x")
print("Q - which language is best for AI\ML\n1.java \n2.python \n3.css \n4.java script")

user_input_2 = int(input("Enter the correct option : "))

match user_input_2:
    case 1:
        print("wrong answer")
    case 2:
        print("correct answer")
        score+= 1
    case 3:
        print("wrong answer")    
    case 4 :
        print("wrong answer")
print("x--------------------x-------------------x------------------x")
print("you got "+str(score)+" questions correct!")
print("x--------------------x-------------------x------------------x")