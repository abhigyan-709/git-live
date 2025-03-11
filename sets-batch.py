basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                        # show that duplicates have been reomved

# Set operations
a = set('abracadabra')
b = set('alacazam')
print("Print the contents of set A: ", a)   
print("Print the contents of set B: ", b)                              # unique letters in b
# print("letters in a but not in b: ", a - b)                          # letters in a but not in b
# print("letters in a or b or both: ", a | b)                          # letters in a or b or both
# print("letters in both a and b: ", a & b)                          # letters in both a and b
print("letters in a or b but not both: ", a ^ b)     # letters in a or b but not both

# # set is represented by curly braces = {}
# # set is mutable in nature
# # set is unordered
# # set does not support indexing
# # set does not support slicing
# # set does not support item assignment
# # set does not support item deletion
# # set does not support duplicate elements
# # we can create empty set using set() function
# s = set()
# print(s, type(s), len(s))


set_a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(set_a)

set_b = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(set_b)

my_set = set()
# if you want to operate something over the list, then convert it to the tuple first and the add it to the set
my_list = [1, 2, 3, 3, 4, 6, 5, 6, 7, 8, 9]
my_list_2 = [1, 2, 3, 3, 4, 6, 5, 6, 7, 8, 9]

my_set.add(tuple(my_list))
my_set.add(tuple(my_list_2))

print("This is my set: ", my_set)

