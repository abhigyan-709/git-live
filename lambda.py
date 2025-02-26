# # # date 26 february

# # def make_incrementor(n):
# #     return lambda x : x + n

# # f = make_incrementor(10)

# # print(f(0))
# # print(f(1))
# # print(f(3))

# # print(f(34))


# add = lambda x, y, z : x + y + z
# print(add(2, 4, 7))


# # calc
# # 1. add, sub, mul, percentage, ----..., (power)
# # 

# # power = lambda x, y : x ** y
# # print(power(2, 3))

# # square of the list of number 
# # numbers = [1, 2, 3, 4, 5]

# # square = list(map(lambda x: x ** 2,numbers))
# # print(square)

operation = { 
    1 : lambda x, y : x + y,
    2 : lambda x, y : x - y,
    3 : lambda x, y : x * y,
    4 : lambda x, y : x ** y
}

calc = int(input("What functionality you want to use, choose - 1/2/3/4: "))
print(operation[calc])
x = input("Value of x: ")
y = input("value of y: ")
print(operation[calc](x, y))

# syntax of the lambda function 
# lambda "arguments" : "expressions"

