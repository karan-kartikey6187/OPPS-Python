from atm import Account
from input import input_validation
class Menu(Account):
     def main_menu(self):   
         while True:
             print(">>>>>>>>}-ATM Menu-{<<<<<<<<")
             print("1.Check Balance.")
             print("2.Withdrawal Money.")
             print("3.Deposit Money.")
             print("4.Exit.")
             
             choice = input("Please Enter Your Choice: ") 
             if choice.isdigit():
                 choice=int(choice)
             else:
                 print("Please enter number only Between(1-3)")
             if choice==1:
                    input_pin=input_validation.check_pin(self)
                    Account.balance_check(self,input_pin)
                
             elif choice==2:
                    input_amount= input_validation.check_Amount(self)
                    if input_amount>0:
                        input_pin=input_validation.check_pin(self)
                        Account.withdrawl(self,input_amount,input_pin)
                    else:
                        print("Transaction failed! Amount must be greater than zero.")      
             
             elif choice==3:
                    input_amount= input_validation.check_Amount(self)
                    if input_amount>0:
                        input_pin=input_validation.check_pin(self)
                        Account.deposit(self,input_amount,input_pin)
                    else:
                        print("Transaction failed! Amount must be greater than zero.")      

             elif choice==4:
                 print("Exit Successfull.")
                 break        