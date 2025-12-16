from main_op import opreration
from databasemodel import FileDetails
json_file=FileDetails.path
ob=opreration(json_file)
ob.main_operation()