# create a dictionary mapping numbers to their squares for numbers 1 to 10
# using dictionary comprehension

squares1 = {}
for x in range(1, 11):
  squares1[x] = x*x
print(squares1)

squares2 = {x:x*x for x in range(1, 11)}
print(squares2)