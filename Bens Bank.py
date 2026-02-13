from datetime import datetime
import os
import hashlib


def openingMenu():
    while True:
        k = input("Type 1 if you have an account, 2 if you want to create one, 3 to exit program ")
        if k == "1":
            login()
            
        elif k == "2":
            createAccount()

            
        elif k == "3":
            print("Exiting program.")
            break
        
        else: print("Invalid input")



def createAccount():
    username = input("What is your username? ")
    
    if os.path.exists("users.txt"):
        with open("users.txt", "r") as f:
            for line in f:
                existing_user = line.strip().split(",")[0]
                if username == existing_user:
                    print("Username already exists.")
                    return
    pin = input("What do you want your PIN to be (4 digits)? ")
    
    hashed_pin = hash_text(pin)
    
    with open ("users.txt", "a") as f:
        f.write(f"{username},{hashed_pin}\n")
        
    print("Account created succesfully!")
        


def hash_text(text):
    return hashlib.sha256(text.encode()).hexdigest()




def login():
    

    while True:
        a = input("Hello welcome to Bens Bank, if you know the word please type 1, if you would like to close the program, type 3. ")
        if a == "1":
            user = input ("Please type your secret word ")
            with open("pass.txt", "r") as f:
                correct_password = f.read().strip()
                
            if hash_text(user) == correct_password:
                print("Correct secret word! ")
                    
                pin = input("Enter your PIN: ")
                username = get_username_from_pin(pin)
                    
                if username:
                    print("Login succesful!")
                        
                    my_bank = Bank(username)
                    transaction = TransactionHistory(username)
                        
                    menu = Menu(my_bank,transaction)
                    menu.aMenu()
                else:
                    print("Invalid PIN.")
                    
            else:
                print("Incorrect secret word, try again.")
        elif a == "3":
            print("Exiting program.")
            break  
        else:
            print("Invalid input, try again.")

def get_username_from_pin(pin):
    hashed_pin = hash_text(pin)
    with open("users.txt", "r") as f:
            for line in f:
              username, stored_pin = line.strip().split(",")
              if hashed_pin == stored_pin:
                  return username
              
    return None
    
#---------------------- BANK CLASS -------------------              

class Bank():
    def __init__(self,username):
        self.username = username
        self.filename = f"{username}_bank.txt"
    
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                f.write("0")
                
    def get_balance(self):
        with open(self.filename, "r") as f:
            return float(f.read())
            
        
    def save_balance(self,balance):
        with open(self.filename, "w") as f:
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
      
#------------- TRANSACTION CLASS ----------------
class TransactionHistory():
              
              
    def __init__(self,username):
        self.username = username
        self.filename = f"{username}_th.txt"
        
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                f.write("Type       Amount               Timestamp        Balance\n")
    def time(self):
        now = datetime.now()                 
        formatted = now.strftime("%Y-%m-%d %H:%M:%S")  
        return formatted
    
    def readHistory(self):
        with open(self.filename, "r") as f:
            return str(f.read())
    
    def writeHistDepo(self,balance,new_balance):
        typen = "Deposit"
        amount = balance
        timestamp = self.time()
        balance = new_balance
        
        with open(self.filename, "a") as f:
            f.write(f"{typen:<10}{amount:>10}{timestamp:>25}{balance:>15}\n")
            
    def writeHistWith(self,balance,new_balance):
        typen = "Withdraw"
        amount = balance
        timestamp = self.time()
        balance = new_balance
        
        with open(self.filename, "a") as f:
            f.write(f"{typen:<10}{amount:>10}{timestamp:>25}{balance:>15}\n")

#------------------- MENU CLASS -------------------

class Menu():
    
    def __init__(self, bank, transaction):
        self.bank = bank
        self.transaction = transaction
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
                print(self.bank.get_balance())
                
            elif a == "2":
                try:
                    
                    value = float(input("How much would you like to deposit? "))
                    
                except ValueError:
                    print("Please input a valid number.")
                    continue
                
                new_balance = self.bank.deposit(value)
                print("Your new balance is", new_balance)
                self.transaction.writeHistDepo(value,new_balance)
                
                
            elif a == "3":
                try:
                    
                    value = float(input("How much would you like to withdraw? "))
                
                except ValueError:
                    print("Please input a valid number.")
                    continue
                
                new_balance = self.bank.withdraw(value)
                print("Your new balance is", new_balance)
                self.transaction.writeHistWith(value, new_balance)
                
            elif a == "4":
                self.user_inactive = True
                
            elif a == "5":
                print(self.transaction.readHistory())
                
            elif a == "6":
                with open(self.transaction.filename, "w") as f:
                    f.write(str("Start of transaction history" "\n"))
                
            else:
                print("invalid input")

openingMenu()
