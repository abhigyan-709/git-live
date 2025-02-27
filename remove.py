orig_list = [1,1, 2, 2, 3, 4, 4, 5,5, 6, 6]
uniq_list = []
for element in orig_list:
    if element not in uniq_list:
        uniq_list.append(element)

print("Original list:", orig_list)
print("List after removing duplicates:", uniq_list)
