from menu import Menu
from Student_Manage_By_Class import student
from read_write import Read_write
class opreration:
    def __init__(self,json_file):
        self.json_file=json_file
        self.student_data=[]
        Read_write.read(self)

    def main_operation(self):
            while True:
                choice = Menu.main_menu(self)
                # try:
                if choice == 1:
                    student.register_opration(self)
                    Read_write.save_data_opration(self) 
                elif choice==2:
                    student.search_opration(self) 
                elif choice==3:
                    student.update_opration(self) 
                elif choice==4:
                        student.delete_opration(self) 
                elif choice == 5:
                    print("Exiting program")
                    break
                else:
                    print("Invalid choice")
                # except Exception:
                #     print("Something went wrong! Please try again.")       