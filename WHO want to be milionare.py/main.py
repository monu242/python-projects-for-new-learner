Questions = [
    ["Q - Who is the prime minster of india:-","Narender modi","Rahul gandhi","Ajay devgan","sharukh khan",1],
    ["Q - what is captital of  india:- ","arunachal pardesh ","delhi","old delhi","west bengal",2],
    ["Q - what is square root of  64:-","9","7","8","2",3],
    ["Q - what is the profession of shah Rukh Khan:- ","Actor","Cricketor","WWE wrestler","hollywood Actor",1],
    ["Q - what is the  capital of japan:-","tokyo","okinawa","paris","delhi",1],
    ["Q - who is the fastest man on planet  Earth:-","speed","usain bolt","david goggins","cheetah",2],
    ["Q - which language is best to learn in 2026 for future and better option and fun:-","python","java script","c","c++",1]

]

prizes = [1000000,20000000,3000000,400000,5000000,6000000,7000000]
i = 0
for question in Questions:
    
    print(question[0])
    print(f"a.{question[1]}")
    print(f"b.{question[2]}")
    print(f"c.{question[3]}")
    print(f"d.{question[4]}")

    # checking the answer {writing function for that}
    a = int(input("enter your answer : {[1 for a],[2 for b],[3 for c],[4 for d]}  ""="))
    import time
    for r in range(10,0,-1):
            print(f"answer will revealed in {r}")
            time.sleep(1)
    if (question[5] == a):
        print("correct answer")

            
            
    else:
        print(f"Incorrect, the correct answer  is {question[5]}")
        print("better luck next time \n")
        break
    print(f"CONGRULATIONS:--- YOU HAVE WON {prizes[i]}")
    i +=1
