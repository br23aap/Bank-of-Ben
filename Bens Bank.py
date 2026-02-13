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
    
    def readHistory(self):
        with open("th.txt", "r") as f:
            return str(f.read())
        
    def writeHistDepo(self,balance):
        b = str(balance)
        a = "Deposit of "
        with open("th.txt", "a") as f:
            f.write(a + b + "\n")
            
    def writeHistWith(self,balance):
        b = str(balance)
        a = "Withdraw of "
        with open("th.txt", "a") as f:
            f.write(a + b + "\n")
                
                
        
user_inactive = False
my_bank = Bank()

#Menu

while not user_inactive:
    print ("Option 1, view balance ")
    print ("Option 2, deposit ")
    print ("Option 3, withdraw ")
    print ("Option 4, exit ")
    print ("Option 5, read transaction history ")
    a = input("... ")

    if a == "1":
        print(my_bank.get_balance())
        
    elif a == "2":
        value = float(input("How much would you like to deposit? "))
        print(my_bank.deposit(value))
        (my_bank.writeHistDepo(value))
        
        
    elif a == "3":
        value = float(input("How much would you like to withdraw? "))
        print(my_bank.withdraw(value))
        (my_bank.writeHistWith(value))
    elif a == "4":
        user_inactive = True
        
    elif a == "5":
        print(my_bank.readHistory())
        
    else:
        print("invalid input")

