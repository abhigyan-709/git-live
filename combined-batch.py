# # function
# # default args
# # keyword args
# # mandatory args
# # postional args

# # deep copy & shallow copy 

# # list.copy()

# # shallow copy - it creates a new object, and references the orginal nested object 
# import copy

# original_list = [[1, 2, 3], [4, 5, 6]]
# shallow_copy_list = copy.copy(original_list)

# print("This is original list: ", original_list)
# print("This is shallow copy list: ", shallow_copy_list)

# shallow_copy_list[1][0] = 10


# print("This is original list: ", original_list)
# print("This is shallow copy list: ", shallow_copy_list)

# # time complexity - O(1)
# # space complexity - O(1)

# student_detail = {
#     "name" : "abhigyan",
#     "batch" : 1,
#     "skills" : ["Python", "k8", "docker", "aws"]
# }

# shallow_copy_list_2 = student_detail.copy()

# print(student_detail)
# print(shallow_copy_list_2)

# print(type(shallow_copy_list_2["skills"]))

# shallow_copy_list_2["skills"].append("java")
# print(student_detail)
# print(shallow_copy_list_2)

# deep copy - completely creates a new object which is independent from parent object
# import copy
# my_list = [[1, 2, 3], [5, 6, 7]]

# deep_copy_list = copy.deepcopy(my_list)
# print("Original Copy: ", my_list)
# print("Orginal Deep Copy: ", deep_copy_list)

# deep_copy_list[1][2] = 9

# print("Original List: ", my_list)
# print("list after deep copy: ", deep_copy_list)


# list comprehensions


# its a concise way to creata a list 
# square = []

# for x in range(10):
#     square.append(x**2)

# print(square)

# square_2 = list(map(lambda x: x ** 2, range(10)))
# print(square_2)

tuples_list = [(x, y) for x in [1, 2, 3] for y in [2, 3, 4] if x != y]
print(tuples_list)

# tuple_list = []
# for x in [1, 2, 3]:
#     for y in [2, 3, 4]:
#         if x != y:
#             tuple_list.append((x, y))
# print(tuple_list)

even_number = [x for x in range(1, 11) if x % 2 == 0]
print(even_number)

even_number2 = []
for x in range(1, 11):
    if x % 2 == 0:
        even_number2.append(x)

# table 2, 3, 4
# [[2, 4, 6, 8, .....], [3, 6, 9, 12....], [4, 8, 12, 16......]]

# dict
dict = {
    2 : 4,
    3 : 9,
    4 : 16,
    5 : 25
}