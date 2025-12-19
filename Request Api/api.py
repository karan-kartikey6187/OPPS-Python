import requests
import json
class Api_data:
    def __init__(self):
        json_response=requests.get("https://openlibrary.org/search.json?q=crime+and+punishment&fields=key,title,author_name,editions")
        self.json_response=json_response.json()
   
class Search_by(Api_data):
    def by_numfound(self):
        key=input("Please Enter Key: ")
        found=False
        for data in self.json_response["docs"]:
            if data["key"]==key:
                print(json.dumps(data,indent=4))
                found=True

        if not found:
           print("No Record Found!")
    
data=Search_by()
data.by_numfound()  