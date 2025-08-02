#Calculator 
print ("-- Welcome to Calculator App--")

ch = "yes "

while ch.lower() !="no":
    try:
        #Input two number
        a = int (input ("Enter first number:"))
        b = int (input ("Enter second number:"))
        
        #Menu for operstions
        print ("\n Choose an operation:")
        print("1 Addition(+)")
        print ("2 Subtraction (-)")
        print ("3 Multiplication(*)")
        print ("4 Divison (/)")

        operation = input ("Enter your choice (1/2/3/4 or +,-,*,/):")
         # Perform the operation
        if operation == '1' or operation == '+':
            result = a + b
            print("Result: ", result)

        elif operation == '2' or operation == '-':
            result = a - b
            print("Result: ", result)

        elif operation == '3' or operation == '*':
            result = a * b
            print("Result: ", result)

        elif operation == '4' or operation == '/':
            if b != 0:
              result = a / b
              print("Result: ", result)
            else:
               print("Error : Division by zero is not allowed.")
        else:
            print("Invalid choice . Please try again.")
    except  ValueError:
        print ("Invalid input. please enter numeric values.")
              
        ch = input ("\n Do you want to continue ? (yes/no):")
        print() 

    print("Thank you for using the calculator app!")   