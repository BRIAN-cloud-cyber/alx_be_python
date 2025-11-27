import datetime

"""
import datetime
----KEY CLASSES---
1>Date (year,month,day) 
today=datetime.date.today()

2>time (HH.MM.SS.MS.TZinfo)
current_time=datetime.tine(10,30,0)

3>datetime -combination of date and time
now=datetime.datetime.now()

4>timedelta -represents a duration,difference btw two date,time,or datetime instances.
-can be used for aritmetic operations with these objects

delta=datetime.timedelta(days=7,hours=3)
future_date=datetime.datetime.now() +delta

--OPERATIONS--
1> formatting: the strftime()-allows formatting date,time,or datetime objects into custom string representations using format codes 
e.g %Y for full year,%m for month number <takes 1>

2>parsing:the strptime() method can parse a string into a datetime object based ona specified format <takes 2 arg>


"""
def display_current_datetime():
     
    #HH.MM.SS
    current_date=datetime.datetime.now()
    
    print(current_date.strftime( "%Y-%m-%m %H-%M-%S"))
display_current_datetime()

def calculate_future_date():
    delta=datetime.timedelta(days=7,hours=3)
    future_date=datetime.datetime.now() +delta
    print(future_date.strftime("%Y-%m-%d"))
calculate_future_date()