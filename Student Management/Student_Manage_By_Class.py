import uuid
import json
from read_write import Read_write
from menu import Menu

class student:
    def register_opration(self):
        print("\n>>>>>>>>>> Registration Details <<<<<<<<<<")
        student = {}
        student["id"] = uuid.uuid4().hex[:6]
        student["name"] = input("Please Enter Your Name: ")
        student["address"] = input("Please Enter Your Address: ")

        while True:
            try:
                contact = int(input("Please Enter Your Contact: "))

                if len(str(contact)) != 10:
                    print("Invalid contact! Enter 10 digit number.")
                    continue

                duplicate = False
                for data in self.student_data:
                    if data["contact"] == contact:
                        print("This Number Already Registered. Enter Another Number.")
                        duplicate = True
                        break

                if duplicate:
                    continue  

                student["contact"] = contact
                break 

            except ValueError:
                print("Enter Only Number Not Character.")

        self.student_data.append(student)
        print("Registration Successful.")

    def input_contact(self):

        while True:
            try: 
                contact =int(input("Please Enter Your Contact: "))
                if len(str(contact)) == 10:
                    break
                else:
                    print("Invalid contact! Enter 10 digit number.")
            except:
                print("Enter Only Number Not Character.")  

        return contact 
    
    
    def search_opration(self):
        if len(self.student_data)>0:
            while True: 
                Menu.search_menu(self)
                try:
                    choice = input("Please Enter Your Choice: ")

                    if choice.isdigit(): 
                        choice = int(choice)
                    else:
                        print("Enter Only Number, Not Character.")  

                    if choice==1:    
                        search_id=input("Please Enter ID: ")                   
                        found=False
                        for data in self.student_data:
                            if data["id"].lower()==search_id.lower():
                                print(json.dumps(data,indent=4))
                                found=True
                        if not found:
                            print("ID not Found")       

                    elif choice==2:    
                        search_contact=student.input_contact(self)                     
                        found=False
                        for data in self.student_data:
                            if data["contact"]==search_contact:
                                print(json.dumps(data,indent=4))
                                found=True
                        if not found:
                            print("Contact not Found")
                    elif choice==3:
                        print(json.dumps(self.student_data,indent=4))        

                    elif choice==4:
                        break  

                    else:
                        print("Enter The Number Between(1-4).")
                        
                except Exception:
                    print("Something went wrong! Please try again.")                
                        
        else: 
            print("\nSorry! No Data Avliable For Search") 

    


    def update_opration(self):
        if len(self.student_data) > 0:
            while True:
                try:
                    print(">>>>>>>>> Update Menu <<<<<<<<<")
                    id = input("Please Enter ID: ")
                    found = False

                    for user in self.student_data:
                        if user["id"].lower() == id.lower():
                            print(json.dumps(user, indent=4))
                            found = True
                            Menu.update_by(self)
                            choice = input("Enter Your Choice: ")

                            if not choice.isdigit():
                                print("Enter only numbers, not characters.")
                                return

                            choice = int(choice)

                            if choice == 1:
                                user["name"] = input("Please Enter New Name: ")
                                Read_write.write_json(self)
                                print("Name updated successfully.")

                            elif choice == 2:
                                user["address"] = input("Please Enter New Address: ")
                                Read_write.write_json(self)
                                print("Address updated successfully.")

                            elif choice == 3:
                                return

                            return

                    if not found:
                        print("ID not found.")

                except Exception:
                    print("Temporary issue occurred! Please try again later.")  
        else:
            print("\nSorry! No data available for update.")

    def input_contact_delete(self):
        try:
            while 1:
                contact = input("Please Enter Contact To Delete: ")
                if len(contact) == 10 and contact.isdigit():
                    return int(contact)
                    break
                else:
                    print("Invalid contact! Enter 10 digit number.")
                    
        except:
            print("Enter Only Number Not Character.")
                  

    def delete_opration(self):    
        if len(self.student_data)>0:        
            while True:
                try:    
                    Menu.delete_by(self)
                    choice = input("Please Enter Your Choice: ")

                    if choice.isdigit(): 
                        choice = int(choice)
                    else:
                        print("Enter Only Number, Not Character.")
                        continue

                    found = False    

                    if choice == 1:
                        i=0    
                        delete_id = input("Please Enter ID: ")                    
                        while i < len(self.student_data):
                            if self.student_data[i]["id"].lower() == delete_id.lower():
                                self.student_data.pop(i)
                                found = True
                            else:
                                i += 1 
                        Read_write.write_json(self)

                                
                    elif choice == 2:
                        i=0
                        delete_contact =student.input_contact_delete(self)
                        while i < len(self.student_data):
                            if self.student_data[i]["contact"] == delete_contact:
                                self.student_data.pop(i)
                                found = True
                            else:
                                i += 1 
                        Read_write.write_json(self)

                    elif choice == 3:
                        return

                    if not found:
                        print("User Not Found!.")
                    if found:
                        print("Deleted Successfully.") 

                except Exception:
                    print("Something went wrong! Please try again.")        
        else: 
            print("\nSorry! No Data Avliable For Delete")         