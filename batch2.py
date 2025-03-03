# # print("Hello World!")

# # a = 6 # int
# # print(a, type(a))

# # b = 7.8 # float
# # print(b, type(b))

# # c = "Abhigyan" # string 
# # print(c, type(c))

# # d = [1, 2, "a"] # list
# # print(d, type(d))

# # e = (1, 2, 4, 5) # tuple
# # print(e, type(e))

# # f = {"name": "Abhigyan" } # key value pair
# # key = "name"
# # value = "Abhigyan"

# # g = (1, 2, 3, 1, 3, 4) 
# # set(g)# set
# # print(set(g), type(g))

# # h = {1, 2, 4, 5, 1, 2, 3, 4, 5} # declaration of sets 
# # print(h, type(h)) # printing the sets

# print(17 + 9)
# print(-3**2)

# print((-3)**2)
# # operator precedence 

# # "-" < "**" "()"

# print(5-9)
# print(2 / 10)
# print(5//9)
# print(4*9)
# # print(1/0)

# program to check the number is even or not

# value = int(input("Please enter the number you want to check: "))
# if value % 2 == 0:
#     print("You entered the even number")

# else:
#     print("Number is odd")

# value = input("Please enter your number: ")
# new_value = float(value)
# new_value_2 = str(value)
# print(new_value, type(new_value))
# print(new_value_2, type(new_value_2))

# string manipulation

# same datatypes operations

# list1 = ["1", 1, "a", 5.4, True]
# print(type(list1))

# tuple1 = ("1", [1, 2, 3], "a", False)
# print(type(tuple1))

# set1 = {1, "a", 1.0}
# print(set1, type(set1))

# dictionary - but a key value pair
# dict1 = {
#     "name" : "abhigyan",
#     "city" : "delhi",
#     "phone" : 1234567890,
#     "percentage" : 89.04,
#     "list_of_tech" : ["python", "aws", "devops"]
# }
# print(type(dict1))
# print(type(dict1.get("list_of_tech")))
# print(type(dict1["phone"]))

# string

# print("Hello World! \nThis is Project DevOps. \nThis is the batch 2 \nNumber of students is 80")

# print("doesn't")
# print('doesn\'t')

# print('"yes",they said')

# print("Hello:\tAbhigyan")

suffix = "thon"
print("py" + suffix)

string = "python"
print(string[-1])

#python indexing 

"""
In python indexing starts from L - R = 0
In python indexing starts from R - L = -1
"""

print(string[-1] == string[5])
"yth"
print(string[1:4])

# strat : stop : step
string2 = "Hello World!"
print(string2[::-1])

# list 

list1 = [1,2, 34, 5]
# list1[0:n+1]
list1[0:5]

print(list1[-3:0])

# upper 
# lower 
# reverse
# filter
# map
# zip

list2 = [1, 2,4, 5, 6,7, 7, 8, 3, 4, 5, 6, 7, 8, 9, 2, 4, 5, 6,7, 8, 9, 0, 4, 3, 3, 8, 3, 4, 5, 6, 7, 8, 9, 2, 4, 5, 6,7, 8, 9, 0, 4, 3, 3, 8, 9, 2, 4, 5, 6,7, 8, 9, 0, 4, 3, 3, 8, 3, 4]

print(list2[-1])


name1 = "simran"
print(name1[::-6])
print(name1[::-5])
print(name1[::-4])
print(name1[::-3])
print(name1[::-2])
print(name1[::-1])
