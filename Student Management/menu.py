class Menu:
    def main_menu(self):
            while True:
                print("\n>>>>>>>>>>>>> Menu <<<<<<<<<<<<<")
                print("1. Register")
                print("2. Search")
                print("3. Update")
                print("4. Delete")
                print("5. Exit")
                try:
                    choice = input("Please Enter Your Choice: ") 
                    if choice.isdigit():
                        return int(choice)
                    else:
                        print("Please enter number only.")
                except Exception:
                    print("Something went wrong! Please try again.")

    def search_menu(self):
            print(">>>>>>>>>>Search<<<<<<<<<<<")
            print("1.Search By ID")    
            print("2.Search By Contact")
            print("3.View All Records")
            print("4.Back")

    def update_by(self):
           print("1. Update Name")
           print("2. Update Address")
           print("3. Back")
           
    def delete_by(self):                    
           print(">>>>>>>>>>>>>>Delete Menu<<<<<<<<<<<<<<")
           print("1. Delete By ID.")
           print("2. Delete By Contact.")
           print("3. Back.")

                
              