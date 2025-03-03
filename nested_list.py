# create a multiplication table (nested list comprehension 2, 3, 4)

mul_table = [[ i * j for j in range(1, 11)] for i in [2, 3, 4]]

print(mul_table)

# create a dictionary mapping number to their squares
dict_num_sq = { i: i ** 2 for i in range(2, 6)}

print(dict_num_sq)
