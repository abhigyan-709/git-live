# 1) CREATE A MULTIPLICATION TABLE OF 2,3,4
n=2
table=list(map(lambda x:[n*x],range(1,11)))
print(table)



# 2) CREATE A DICTIONARY MAPPING NUMBER TO THEIR SQAURE

square_of_number={} #expanded way
for i in range(1,10):
    sq=i**2
    square_of_number[i]=sq
print(square_of_number)


dict={x:x**2  for x in range(10)} #concise way 
print(dict)
