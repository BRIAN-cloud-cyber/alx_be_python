def perform_operation(num1:float ,num2:float,operation:str ):
    if operation=="add":
        return num1 + num2
    elif operation=="subtraction":
        return num1 - num2
    elif operation=="multiply":
        return num1 *num2
    elif operation=="division":
        try:
            return num1 /num2
        except ZeroDivisionError:
            return ("Invalid Values")
     
perform_operation()

