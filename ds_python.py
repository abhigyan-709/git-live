# indentation - 4 
# max chars - 79 
# docstrings 

# def add(a, b):
#     """This is the doc string for the add function.
#     This can be also used for documentation.
#     """

#     return a + b

# add2 = add(6, 7)
# print(add2)
# print(add.__doc__)


# data structures
# append 
# list1 = [1, 2, 4, 5, 6]
# list2 = [3, 4, 5, 6]

# list3 = list1 + list2
# print(list3)

# list3.append(8)
# print(list3)

# # extend 

# l1 = [1, 2, 5, 6]
# l2 = [6, 4, 3, 1]

# l1.extend(l2)
# print(l1)
# l2.extend(l1)
# print(l2)

# # insert 
# # given point of index kisi bhi element ko add karne mein 

# new_list = [1, 3, 5, 7, 0]
# new_list.insert(2, 6)
# print(new_list)

# remove
# list.remove(x) where x is the element of the list
# it will remove only the first occurance of the value equal to x or element found in the list 
# new_list2 = [1, 2, 1, 3, 4, 5, 6, 1, 4, 5, 6 ,8 , 9]
# new_list2.remove(1)
# print(new_list2)

# new_list2.remove(1)
# print(new_list2)

# new_list2.remove(0)
# print(new_list2)

# list.pop([i])
# .pop removes the item at the given point or position in th list

# list1 = [1, 2, 3,4, 6, 7, 8]
# list1.pop()
# print(list1)

# list1.pop(1)
# print(list1)

# list.clear() == del list[:]

# list1 = [1, 2, 3, 4]
# list2 = [1, 2, 3, 4]

# list1.clear()
# print(list1, len(list1))

# del list2[:]
# print(list2, len(list2))

# list.index 
# list.index(element, start, stop)
# its use is to find the first occurance of the specific element

# name = ["abhigyan", "sabhrant", "dipti", "manisha", "rangish", "sabhrant"]
# index_sabhrant = name.index("sabhrant", 2, 6)

# print(index_sabhrant)

# list2 = [1, 2, 3, 1, 2, 1, 1, 2, 3, 4, 4, 3, 2, 1]
# # no 2 occurance can be found 

# list_index = list2.index(1, 7, 14)
# print(list_index)

# list.count(x)
# count the occurance of the x element in the list
# list2 = [1, 2, 3, 4, 1, 2, 4, 5, 1, 3]
# list3 = list2.count(3)
# print(list3)

# list.sort() default ascending order
# list1 = [3, 4, 5, 1, 2, 3, 5, 8, 3, 4, 5]
# list1.sort()
# print(list1)

# # in decending order
# list2 = [3, 4, 5, 1, 2, 3, 5, 8, 3, 4, 5, 9]
# list2.sort(reverse=True)
# print(list2)

# sort the list 
stringify = ["a", "ab", "abc", "bc", "bcad", "bca", "abcd", "qrs", "poutl"]

# by default
stringify.sort(key=len)
print(stringify)
