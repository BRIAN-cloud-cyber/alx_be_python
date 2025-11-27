FAHRENHEIT_TO_CELSIUS_FACTOR=5/9
CELSIUS_TO_FAHRENHEIT_FACTOR=9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit-32)* FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
     return(celsius*CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    
def main():
    try:
        temperature_to_be_converted= float(input("Enter temperature to be converted: "))
        unit_check=input(" Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit_check =="F":
            converted=convert_to_celsius(temperature_to_be_converted)
            print(f"{temperature_to_be_converted} F is {converted} C")

        elif unit_check=="C":
            converted=convert_to_fahrenheit(temperature_to_be_converted)
            print(f"{temperature_to_be_converted}C is {converted} F ")
        else:
         return ("Invalid unit.Please choose between (C/F)")
    except ValueError:
        raise ValueError("Invalid temperature.Please enter a numeric value")
    
if __name__=="__main__":
    main()
