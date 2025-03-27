list1 = [3, 5, 7, 2, 5]

min_value = list1[0]
max_value = list1[0]

for num in list1:
    if num < min_value:
        min_value = num
    elif num > max_value:
        max_value = num

print(f"Maxmimum value in '{list1}' is '{max_value}'")
print(f"Minimum value in '{list1}' is '{min_value}'")
