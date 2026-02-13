from datetime import datetime

class Bank():
    def get_balance(self):
        with open("bank.txt", "r") as f:
            return float(f.read())
            
        
    def save_balance(self,balance):
        with open("bank.txt", "w") as f:
            f.write(str(balance))
        
        
    def deposit(self,amount):
        self.balance = self.get_balance()
        self.balance += amount
        self.save_balance(self.balance)
        return self.balance
    
    def withdraw(self,amount):
        self.balance = self.get_balance()
        self.balance -= amount
        self.save_balance(self.balance)
        return self.balance
    
    
    
class TransactionHistory():
    
    def time(self):
        now = datetime.now()                 
        formatted = now.strftime("%Y-%m-%d %H:%M:%S")  
        return formatted
    
    def readHistory(self):
        with open("th.txt", "r") as f:
            return str(f.read())
    
    def writeHistDepo(self,balance,new_balance):
        typen = "Deposit"
        amount = balance
        timestamp = self.time()
        balance = new_balance
        
        with open("th.txt", "a") as f:
            f.write(f"{typen:<10}{amount:>10}{timestamp:>25}{balance:>15}\n")
            
    def writeHistWith(self,balance,new_balance):
        typen = "Withdraw"
        amount = balance
        timestamp = self.time()
        balance = new_balance
        
        with open("th.txt", "a") as f:
            f.write(f"{typen:<10}{amount:>10}{timestamp:>25}{balance:>15}\n")
                
                
        

my_bank = Bank()
transaction = TransactionHistory()


#Menu



class Menu():
    
    def __init__(self):
        self.user_inactive = False
    
    def aMenu(self):
        while not self.user_inactive:
            print ("Option 1, view balance ")
            print ("Option 2, deposit ")
            print ("Option 3, withdraw ")
            print ("Option 4, exit ")
            print ("Option 5, read transaction history ")
            print ("Option 6, wipe transaction history ")
            a = input("... ")

            if a == "1":
                print(my_bank.get_balance())
                
            elif a == "2":
                value = float(input("How much would you like to deposit? "))
                new_balance = my_bank.deposit(value)
                print("Your new balance is", new_balance)
                transaction.writeHistDepo(value,new_balance)
                
                
            elif a == "3":
                value = float(input("How much would you like to withdraw? "))
                new_balance = my_bank.withdraw(value)
                print("Your new balance is", new_balance)
                transaction.writeHistWith(value, new_balance)
                
            elif a == "4":
                self.user_inactive = True
                
            elif a == "5":
                print(transaction.readHistory())
                
            elif a == "6":
                with open("th.txt", "w") as f:
                    f.write(str("Start of transaction history" "\n"))
                
            else:
                print("invalid input")
menu = Menu()
menu.aMenu()

