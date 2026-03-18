try:
    a = int(input("Enter the first value [a]:"))
    b = int(input("Enter the  second value [b]: "))
    
    print("Calculator OPERATIONS :- \n 1.press + for addition.\n 2.press - for subtraction.\n 3.press / for division.\n 4.press * for multiplication. ")
    
    #using input for operation 
     
    o = input("enter the name of  the operation: ")

    match o:
        case "+":
            print(f"The result of the  function is {a+b}")
        case "-":
            print(f"The result of the  function is {a-b}")
        case "/":
            print(f"The result of the  function is {a/b}")
        case "*":
            print(f"The result of the  function is {a*b}")
        case default:
            print("This type of operation is not available in this calculator [wait for update !]")
except ZeroDivisionError:
    print("the result of the function is infinity")

except ValueError:
    print("enter the meaningful values for this operation")

except Exception as e:
    print("The operation is not working .[sorry]")

print("YEAH ! the operation has worked")
    
