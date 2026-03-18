# project maded by me it is a python code for the normal to do list 




import time


print("-------TO DO LIST------------")


main_task= []

n = int(input("Enter the number of the main task do you want to add : "))

for i in range (n):
    tasks = input(f"Enter the main task {i+1} : ").lower()
    main_task.append(tasks)

    print("\n Main tasks are :")
    for t in main_task:
        print("-",t)# t is the tasks in the main taks sets


timer = int(input("enter the timer you  want to set [in minutes]:  "))


seconds = timer*60
print("\n-----------------Timer starts now------------------------------------")
time.sleep(seconds)
print("\n------------------------Timer ends now------------------")

completed_tasks = []

m = int(input("Enter the number of task you completed :  "))
for _ in range (m):
    tasks_c = input(f"Enter the task {_+1}:  ").lower()
    completed_tasks.append(tasks_c)

#checking if every task is completed or not 

if set(main_task).issubset(completed_tasks):
    print("congo! every task is done")
else:
    print("Some tasks are still pending")

print("\n program ends")
