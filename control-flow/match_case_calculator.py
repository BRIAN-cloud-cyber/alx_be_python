#match_case_calculator
while True:
    
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))

    # ask for the operation
    operation = input("Choose an operation (+,-,*,/): ")

    match operation:
        case "+":
            result = number1 + number2
            print(f"The result of {number1} + {number2} is {result}.")
        case "-":   
            result = number1 - number2
            print(f"The result of {number1} - {number2} is {result}.")
        case "*":    
            result = number1 * number2
            print(f"The result of {number1} * {number2} is {result}.")
        case "/":    
            if  number2==0:
                print("Error: Division by zero is not allowed.")
            else:
                result = number1 / number2
                print(f"The result of {number1} / {number2} is {result}.")
        case _:    
            print("Invalid operation selected.")
