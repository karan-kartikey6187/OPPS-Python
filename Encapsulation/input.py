class input_validation:
    def check_Amount(self):
        while True:
            amount= (input("Please Enter Amount: "))
            if amount.isdigit():
                return(int(amount))
                break
            else:
                print("Invalid Amount!")

    def check_pin(self):
        while True:
            pin= (input("Please Enter PIN: "))
            if pin.isdigit():
                return(int(pin))
                break
            else:
                print("Invalid PIN!")        