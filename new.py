list1 = [3,5,7,2,5]


largest= list1[0]
smallest=   list1[0]

for num in list1:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

        print("Largest number:", largest)
        print("Smallest number:", smallest)