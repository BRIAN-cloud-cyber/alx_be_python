 
# Future Age Calculator
"""
current_age = int(input("How old are you? "))
future_age = current_age + 27

print(f"In 2050, you will be {future_age} years old.")
"""

from datetime import datetime

#year_of_birth=int(input("enter year of birth : "))

current_year=datetime.now().year

age= int(input("enter your age: "))
year_of_birth=current_year - age    

print(f"you were born in the year {year_of_birth}")
