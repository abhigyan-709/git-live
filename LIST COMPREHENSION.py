n=int(input("ENTER NUMBER:"))
list_1=[]
#Printing List Without List Comprehension!!!
for i in range(1,11):
    list_1.append(n*i)
print("LIST WITHOUT COMPREHENSION:",list_1)
#Printing List With List Comprehension
list_1=[n*i for i in range(1,11)]
print("LIST WITH COMPREHENSION:",list_1)

