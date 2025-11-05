while True:
    print("Welcome to your calculator")
    print("1.Addition")
    print("2.Subtaction")
    print("3.Multiplication")
    print("4.Division")
    Operator = [1,2,3,4]
    choice = int(input("Enter your choice(1/2/3/4): "))
    if choice not in Operator:
        break
    num1 = float(input("Enter your first number: "))# i want to repeat the question if user put wrong value 
    num2 = float(input("Enter your second number "))
    if choice == 1:
        print(f"Addition of {num1} and {num2} is: ",num1+num2)
    elif choice == 2:
        print(f"Subtaction of {num1} and {num2} is: ",num1-num2)
    elif choice == 3:
        print(f"Multiplication of {num1} and {num2} is: ",num1*num2)
    elif choice == 4:
        if num2!=0:
            print(f"Division of {num1} and {num2} is: ",num1//num2)
        else:
            print("Please give valid number, Try Again!")
    else:
        print("Please choose right operater")
    print("Solve your next problem")
        
        
        
        







    
        
