poem = ["marry", "has", "a", "little", "lamb"]
# # print(len(poem))
# # print(len(poem[1])) # at index 1 "has" is element 

# for p in poem:
#     print(p, len(p))

# range function 
# range(start, stop, step)

# for p in range(len(poem)): # range(5)
#     print(p, poem[p])

# for i in range(10):
#     print(i)

# print(list(range(1, 11, 2)))

# print(list(range(-10, -112, -20)))

# ap : 1, 90, 3
#print("Sum of the AP is: ", sum(range(1, 91, 3)))

# break & continue

# break when condition matches, it gets out of loop
# for num in range(1, 10):
#     if num == 5:
#         print("Breaking the Loop")
#         break
#     print(num)

# print("Loop Ended")

# for num in range(1, 9):
#     if num == 10:
#         print("Breaking the Loop")
#         break
#     print(num)

# continue statement

# for num in range(1, 20):
#     if num == 16:
#         continue
#     print(num, end= ' ')

# print("Loop ended with continue")


# for num in range(1, 10):
#     if num > 5 and num % 2 == 0:
#         print("Break occured at: ", num)
#         break
#     print(num, end=' ')

# print("End of loop")

# else clause in for loop
for n in range(2, 10):
    for x in range(2, n):
        if n % 2 == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')
