# Example list with duplicates
original_list = [1,1 2, 2, 3, 4, 4, 5,5, 6, 6]

# Create a unique list
unique_list = []
for element in original_list:
    if element not in unique_list:
        unique_list.append(element)

# Print the results
print("Original list:", original_list)
print("List after removing duplicates:", unique_list)
