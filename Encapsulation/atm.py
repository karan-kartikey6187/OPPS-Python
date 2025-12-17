class Account:
    def __init__(self):
        self.account_number=256432011223544
        self.__balance=20000
        self.__pin=6789

    def withdrawl(self,amount,pin):
        if pin == self.__pin:
            balance=self.__balance-amount
            if balance>=0:
                self.__balance=balance
                print(f"{amount} Withdraw Successfully.")
                print(f"Now Your Balance Is: {self.__balance}")
            else:
                print("Sorry Insufficient Balance!")    
        else:
            print("Incorrect Pin! Please Enter Valid Pin.")

    def balance_check(self,pin):
        if pin == self.__pin: 
            print(f"Account Number: {self.account_number}") 
            print(f"Balance: {self.__balance}") 
        else:
            print("Incorrect Pin! Please Enter Valid Pin.")

    def deposit(self,add_amount,pin):
        if pin == self.__pin:
           balance=self.__balance+add_amount
           self.__balance=balance
           print(f"{add_amount} Deposit Successfully!")
           print(f"Now Your Balance Is: {self.__balance}")
        else:
            print("Incorrect Pin! Please Enter Valid Pin.")

