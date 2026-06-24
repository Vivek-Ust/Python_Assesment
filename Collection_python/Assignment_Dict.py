# Exercise 1: Perform basic dictionary operations
def dic_basicoperation(data):
    #add new items
    data["city"] = "Banglore"
    print("Add new item:",data)
 
    #update value
    for k, v in data.items():
        if k == "name":
            data[k] = "Vivek"
    print("Update Value",data)
 
    #print keys and values
    print("Keys:", data.keys())
    print("Values:", data.values())
 
    #Length of dictionary
    print("Length of dictionary",len(data))
 
dic_basicoperation({"name":"Vivek", "employee_code":305381, "course":"Python"})
 
#Exercise 2: Perform dictionary operations
def dic_operation(data):
    #get operation
    print(data.get("name"))
    print(data.get("place", "Not found"))
 
    #setdefault
    data.setdefault("city", "Banglore")
    data.setdefault("age", 27)
    print(data)
 
    #update
    data.update({"Organization":"UST"})
    print(data)
dic_operation({"name":"Vivek", "employee_code":305381, "course":"Python"})
 
#Exercise 3: Dictionary from Lists
def dict_list(dic):
    print("Dictionary from Lists:",list(dic.items()))
dict_list({"name":"Vivek", "employee_code":305381, "course":"Python"})
 
#Exercise 4: Clear Dictionary
def dict_clear(data):
    data.clear()
    print("Clear Dictionary: ",data)
dict_clear({"name":"Vivek", "employee_code":305381, "course":"Python"})
 
def mergedic(dict1, dict2):
    dict1.update(dict2)
    print(dict1)  
    #OR
    print(dict1 | dict2) #Modern Python merge (Union Operator)
mergedic({"name": "Alice", "age": 25}, {"city": "New York", "job": "Engineer", "name": "Alice"})
 
#Exercise 6: Count Character Frequencies
def count_char(str):
    dic = {}
    lower = str.lower()
    for i in lower.split(" "):
        dic[i] = dic.get(i, 0) + 1
    print(dic)
count_char("To be or not to be that is the question To be")
 
#Exercise 7: Access Nested Dictionary
def access_dict(data):
    print("Access Nested Dictionary:")
    print(data["a"])
    print(data["a"]["c"])
access_dict({'a':{'b':7, 'c':4}, 'd':5})
 
#Exercise 8: Print the value of key ‘history’ from nested dict
def val_hictory(data):
    if data["employement"]["History"]:
        print(data["employement"]["History"])
    else:
        print("data not found")
val_hictory({"name":"Vivek", "employement":{"History": "LTTS", "Current":"UST"}})
 
#Exercise 9: Modify Nested Dictionary
def modify_nested(data):
    data["details"]["City"] = "Bangalore"
    data["employement"]["Experience"] = 3.5
    print("Modify Nested Dictionary:",data)
modify_nested({"name":"Vivek", "employement":{"History": "LTTS", "Current":"UST"}, "details":{"City":"Hubli", "Domain":"Embedded"}})
 
#Exercise 10: Initialize dictionary with default values
def initialize_defaul_val(lst):
    new  = dict.fromkeys(lst, 10)
    print("Initializing dictionary with default values:",new)
initialize_defaul_val(['a', 'b', 'c'])
 
#Exercise 11: Create a dictionary by extracting the keys from a given dictionary
def new_dict(data):
    key = ["name", "city", "course"]
    new_dict = {i:data[i] for i in key}
    print("New dictionary from extracting the keys from a given dictionary",new_dict)
new_dict({'name': 'Vivek', 'employee_code': 305381, 'course': 'Python', 'city': 'Banglore', 'age': 27})
 
#Exercise 12: Delete a list of keys from a dictionary
def del_dict(data):
    print("Original:", data)
    remove_key = ['employee_code', 'age', 'course']
    for i in remove_key:
        data.pop(i, None)
    print("Delete a list of keys from a dictionary:", data)
del_dict({'name': 'Vivek', 'employee_code': 305381, 'course': 'Python', 'city': 'Banglore'})
 
#Exercise 13: Check if a value exists in a dictionary
def check_val(dic):
    if 'Banglore' in dic.values():
        print("Value 'Banglore' exists in a dictionary")
    else:
        print("Value 'Banglore' doesnot exists in a dictionary")
check_val({'name': 'Vivek', 'course': 'Python', 'city': 'Banglore'})
 
#Exercise 14: Rename key of a dictionary
def rename_key(data):
    data["first name"] = data.pop("name")  # dict[new_val] = dict.pop[old_val] and it will add at the end
    print("Renaming key: ",data)
rename_key({'name': 'Vivek', 'course': 'Python', 'city': 'Banglore'})
 
#Exercise 15: Get the key of a minimum value
def minimum(data):
    new = min(data, key=data.get)
    print("key of a minimum value: ",new)
    print("Minimum value:", data[new])
minimum({'c':51, 'd':13, 'a':37, 'e':74})
 
#Exercise 16: Change value of a key in a nested dictionary
def change_val_nested(data):
    data["a"]["c"] = 96
    print("Change value of a key in a nested dictionary",data)
change_val_nested({'a':{'b':7, 'c':4}, 'd':5})
 
#Exercise 17: Invert Dictionary
def invert_dict(data):
    temp={}
    for k, v in data.items():
        temp[v] = k
    print(temp)
invert_dict({'c':43, 'd':13, 'a':37, 'e':74})
 
#Exercise 18: Sort Dictionary by Keys
def sort_dict_key(dic):
    sort_key_asc = sorted(dic.items(), key = lambda x:x[0])
    sort_key_des = sorted(dic.items(), key = lambda x:x[0], reverse=True)
    print("Sort Dictionary by Keys in ascending order:",dict(sort_key_asc))
    print("Sort Dictionary by Keys in descending order:",dict(sort_key_des))
sort_dict_key({'c':51, 'd':13, 'a':37, 'e':74})
 
#Exercise 19: Sort Dictionary by Values
def sort_dict_val(data):
    sort_val_asc = sorted(data.items(), key = lambda x:x[1])
    sort_val_des = sorted(data.items(), key = lambda x:x[1], reverse=True)
    print("Sort Dictionary by Values in ascending order:",dict(sort_val_asc))
    print("Sort Dictionary by Values in descending order:",dict(sort_val_des))
sort_dict_val({'c':51, 'd':13, 'a':37, 'e':74})
 
#Exercise 20: Check if All Values are Unique
def unique_val(data):
    new = list(data.values())
    if len(new) == len(set(new)):
        print("All Values are Unique")
    else:
        print("All Values are not Unique")
unique_val({'a':15, 'b':67, 'c':15, 'd':20, 'd':20})
unique_val({'c':51, 'd':13, 'a':37, 'e':74})
 