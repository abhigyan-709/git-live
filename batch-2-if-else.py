# # control flow statements!

# # if 
# # nested if
# # if else
# # ladder if - elif
# # match & case - new 3.11 [feature extracted from C]

# # if 

# # lets check and odd and even number

# # n = int(input("Please enter the number: "))
# # if n % 2 == 0:
# #     print("Number is Even")

# # else:
# #     print("Number is Odd")

# # n = int(input("Please enter the digit: "))
# # if n < 0:
# #     print("You entered n: ", n)
# #     n = 0
# #     print("You entered the digit n: ", n)
# # elif n == 1:
# #     print("You enetered n : ", n)
# # elif n % 2 == 0:
# #     print("You entered n: ", n, "Which is an even number.")
# # else:
# #     print("You entered the digit n: ", n, "which is an odd number.")

# # nested if

# # x = int(input("Enter the digit: "))
# # if x == 0:
# #     if x % 2 == 0:
# #         print("X is an even number")
# #     else:
# #         print("X is an odd number.")
# # elif x % 2:
# #     print("X is even: ", x)

# # string = "lceuynouirynweoiurycqoirugyntoiurhbeoiutvyhotinhoivuerytoiuyvqniouryqvwnoriutyvoiuqytbrevoq"
# # print(len(string))

# # list1 = [1,2,4,5,67,8,9, 9]
# # print(len(list1))

# # for loop 

# list1 = ["dog", "cat", "elephant", "lion"]

# users = {
#     "abhigyan" : "active",
#     "manisha" : "inactive",
#     "dipti" : "active", 
#     "user1" : "inactive",
#     "user2" : "active"
# }
# print(users)

# for user, status in users.items():
#     if status == "inactive":
#         del users[user]

# print(users)



# the range function

# if else

# n = int(input("Enter the Number you want to print: "))
# if n % 2 == 0:
#     print("Number is even: ", n)

# elif n == 0:
#     print("You have entered the number 0")

# else:
#     print("Please try again.")



# nested if

l1 = [1, 2, 3, 4, 5]
n = int(input("Enter the number: "))

if n in l1:
    if n % 2 == 0: # nested if
        print("Number is Divisible by 2, and its an even number.")
    else: 
        print("Number is odd")
else:
    print("Number is not in the list")

