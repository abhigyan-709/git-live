# dictionaries in python

# dictionary is a collection of key-value pairs

# dict()
 # creating the dictionary 

import copy
student_details = {
    "name" : "Abhigyan",
    "course" : "Python & DevOps",
    "mobile" : "1234567890"
}

copied_details = copy.deepcopy(student_details)

# print(student_details, type(student_details))
# print(student_details["name"], type(student_details["name"]))

# # addition of elements in the dict.

# student_details["age"] = 27
# student_details["gender"] = "Male"

# print(student_details)

# # delting the objects in dictionary 

# age = student_details.pop("age")
# print(student_details)

# # deleting the last key value : value pair

# last_item = student_details.popitem()
# print(student_details)

# # deleting the whole dictionary 
# student_details.clear()
# print(student_details)
# print(copied_details)


# iterate over the keys
for key in copied_details:
    print(key, copied_details[key])

# iterating over values

for value in copied_details.values():
    print(value)

# 3.9 ++

student_detail = {
     "name" : "Abhigyan",
    "course" : "Python & DevOps",
    "mobile" : "1234567890"
}

education = {
    "maths" : 7.90,
    "networks" : 6.78
}

merged_details = student_detail | education
print(merged_details)


# print dictionary with the 
# 0 : 0, 1 : 1, 2 : 4, 3 : 9

squared_dictionary = {x : x ** 2 for x in range(10)}
print(squared_dictionary)

# print all the keys in dictionry 
keys = merged_details.keys()
print("Keys in Merged Details: ", keys)

values = merged_details.values()
print("Values in the Merged Details: ", values)

items = merged_details.items()
print("Items in Merged Details: ", items, type(items))


# creating the disctonary 

my_list = ["name", "age", "city", "number"]
my_list_value = ["Abhigyan", "27", "Delhi", "1234567890", "male"]

default_dict = dict.fromkeys(my_list, "Unknown")
print(default_dict)

# zip to create the dictionary with the key value pair in the list 
new_dict = dict(zip(my_list, my_list_value))
print(new_dict)

dict_dict = {
    "student1" : { "name" : "Aman", "age" : 18, "city" : "Muzaffarpur"},
    "student2" : { "name" : "Harsh", "age" : 19, "city" : "Mumbai" }
}

print(dict_dict["student1"]["name"])

# count the frequency in the string 

"hello"

sample = {
    "h" : 1,
    "e" : 1,
    "l" : 2,
    "o" : 1
}