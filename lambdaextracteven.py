def even_numbers(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(even_numbers(nums))  

