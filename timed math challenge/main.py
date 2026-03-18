import random 
import time



Operation = ["+","-","*"]
MIN_OPERAND= 3
MAX_OPERAND = 12
TOTAL_PROBLEM = 10



def generate_problem():
    left= random.randint(MIN_OPERAND,MAX_OPERAND)
    right = random.randint(MIN_OPERAND,MAX_OPERAND)
    operator = random.choice(Operation)


    expr = str(left) +" "+operator+"  "+str(right)
    
    answer = eval(expr)# eval is the funcition which as it identify python code and perform it 
    # helpful rather making code long usinng if and else statements ..
    return expr,answer


wrong = 0
input("Press Enter to start !")
print("----------------------x-----------------")

start_time = time.time()

for i in range(TOTAL_PROBLEM):
    expr,answer = generate_problem()
    while True:
       guess = input("Problem #"+str(i+1)+": "+expr+"= ")
       if guess == str(answer):
           break
       wrong+= 1




end_time = time.time()
total_time =  end_time- start_time
print("----------------------x-----------------")
print(f"Nice work ! you finshed in {int(total_time)} seconds " )

