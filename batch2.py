# # # print("Hello World!")

# # data types in python
# # int
# # float
# # string
# # list
# # tuple
# # set
# # dictionary
# # boolean

# a = 6 # int
# print(a, type(a))

# b = 7.8 # float
# print(b, type(b))

# c = 'Abhigyan' # string 
# print(c, type(c))

# # list - but its an array in other languages
# d_1 = [1, 6.6, "ayushi", 'akshay', True, False, (1, 2, 3, 4), {1, 2, 1, 2}]

# print(d_1, type(d_1), type(d_1[6]))

# e = (1, 2, 4, 5) # tuple
# print(e, type(e))

# f = {"name": "Abhigyan" } # key value pair
# # what is dictionary - key value pair

# dict1 = {
#     "name" : "abhigyan",
#     "city" : "delhi",
#     "phone" : 1234567890,
#     "percentage" : 89.04,
#     "list_of_tech" : ["python", "aws", "devops"],
#     "other_details" : {
#         "address" : "delhi",
#         "pincode" : 110001
#     }
# }

# print(dict1, type(dict1))

# g = (1, 2, 3, 1, 3, 4) 
# set(g)# set
# print(set(g), type(g))

# g_1 = {1, 2, 4, 121, 12, 12, 1, 2, 4}
# print(g_1)

# h = {1, 2, 4, 5, 1, 2, 3, 4, 5} # declaration of sets 
# print(h, type(h)) # printing the sets


# python as a calcultor
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
# escape sequence
# print("doesn't")
# print('doesn\'t')

# print("Doesn't")
# print('Doesn\'t')

# print('"yes",they said')
# # escape sequences - \n new line \t - tab
# print("Hello:\tAbhigyan")

# suffix = "thon"
# print("py" + suffix)

# prefix = "abhi"
# suffix = "gyan"

# print(prefix + suffix)

# print(6 * "a")

# # indexing and slicing of the string and lists

# new_string = "a" + "b" + "c"
# old_string = "ab"
# print(new_string)

name = "abhigyan" 
#[0 : a, 1 : b, 2 : h, 3 : i, 4 : g, 5 : y, 6 : a, 7 : n]


print("length of the name: ", len(name))

print("Last character: ", name[-1])
print("last character: ", name[7])

random_char = "kBUGREIRCYUNEOIWRNQWY ORQWRCNOQIWTUYNO ITRYRICUNTYOITN UWYUIEYXONY   E   IRXEOCRIEHWRICNHOIXUWEHO    IU3Y4BROI37YCNOI42HYC OI4HPUIOsO HRWVOTIUNH5OVTIUHW WOTIU W5HOIT"
a = len(random_char)
print("Length of random character: ", a)
print(random_char[a-1])

b = random_char[-1]
print("Last character: ", b)


# left to right - indexing start from 0
# right to left - indexing start from -1



# # list #range function - [start : stop : step]
# print(name[0])

# # from left to right -> 0


# print(name[::-1])





# string = "python"
# print(string[-1])

# #python indexing 

# """
# In python indexing starts from L - R = 0
# In python indexing starts from R - L = -1
# """

name = "abhigyan"
print(name[-1] == name[7])

# "yth"
# print(string[1:4])

# # strat : stop : step
# string2 = "Hello World!"
# print(string2[::-1])

# # list 

list1 = [1, 2, 3, 5, 3, 4, 5, 1, 2, 4, 5]
print(list1)
# list1[0:n+1]

# [0 : n] n = 3
print(list1[0:4])



# new_list = list1[0:2]
# print(new_list)
# # print(list1[-3:0])

# # upper 
# # lower 
# # reverse
# # filter
# # map
# # zip

# list2 = [1, 2,4, 5, 6,7, 7, 8, 3, 4, 5, 6, 7, 8, 9, 2, 4, 5, 6,7, 8, 9, 0, 4, 3, 3, 8, 3, 4, 5, 6, 7, 8, 9, 2, 4, 5, 6,7, 8, 9, 0, 4, 3, 3, 8, 9, 2, 4, 5, 6,7, 8, 9, 0, 4, 3, 3, 8, 3, 4]

# print(list2[-1])


# name1 = "simran"
# print(name1[::-6])
# print(name1[::-5])
# print(name1[::-4])
# print(name1[::-3])
# print(name1[::-2])
# print(name1[::-1])
