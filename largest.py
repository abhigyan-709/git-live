def second_largest(num):
    num.sort()
    return num[-2]

numbers=[4,2,9,6,5,1]
print(second_largest(numbers))