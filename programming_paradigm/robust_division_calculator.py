def safe_divide(numerator,denominator):
    try:
        num=float(numerator)
        den=float(denominator)
        result=num/den
        return result
    except ValueError:
        return ("Invalid input: Please provide a numeric value")

    except ZeroDivisionError:
        return("Error: division by zero is not allowed ")

print(safe_divide(10,0))