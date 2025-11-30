class BankAccount:
    
    def __init__(self,current_balance=0):
        self.balance=account_balance
        
    def deposit(self,amount):
        self.current_balance +=amount 

    def withdraw (self,amount):
         if amount <=self.account_balance:
             self.current_balance -=amount
             return True 
         else:
             return False 
         
    def display_balance(self):
        print(f"Current balance:{self.current_balance}")

    

user1=BankAccount()

