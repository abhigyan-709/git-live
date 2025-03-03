
#Reverse the string without using python build in function 
# user - Ajay singh

def revers(str):
    temp = ''
    for i in range(len(str)-1,-1,-1):
        temp += str[i]
    print(temp)
user_input = str(input("Enter the string: "))
revers(user_input)