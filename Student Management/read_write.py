import os
import json
class Read_write:
    def read(self):
        
        if os.path.exists(self.json_file):
            try:
                with open(self.json_file, "r") as f:
                    self.student_data = json.load(f)
            except:
                self.student_data = []
        else:
            self.student_data = []
                    
    def write_json(self):
        try:
            with open(self.json_file,'w') as file:
                        file.write(json.dumps(self.student_data,indent=4))
        except Exception:
            print("System is busy! Please try again shortly.")  

    def save_data_opration(self):
        try:
            with open(self.json_file, "w") as f:
                f.write(json.dumps(self.student_data, indent=4))
        except Exception:
            print("System is busy! Please try again shortly.")                         