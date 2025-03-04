matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8], 
    [9, 10, 11, 12]
]

# t_matrix = [
#     [1, 5, 9],
#     [2, 6, 10], 
#     [3, 7, 11],
#     [4, 8, 12]
# ]


# normal functionality - 1

# transposed = []

# for i in range(4):
#     transposed.append([row[i] for row in matrix])

# print(transposed)

# normal functionality - 2

# transposed = [] 4 x 3
# for i in range(4):
#     # following 3 lines implement the list comprehension
#     transposed_row = []
#     for row in matrix:
#         transposed_row.append(row[i])
#     transposed.append(transposed_row)

# print(transposed)

# list comprehension 

# transposed = [
#     [row[i] for row in matrix] for i in range(4)
#     ]
# print(transposed)

# zip - unpacking arguments list - "*"
transposed = list(zip(*matrix))
print(transposed)

