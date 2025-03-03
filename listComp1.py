# create a multiplication list of 2,3,4 nested list comprehension

multiList1 = []
for x in range(2, 5):
  innerList=[]
  for y in range(1, 11):
    innerList.append(x*y)
  multiList1.append(innerList)
print(multiList1)

multiList2 = [[x*y for x in range(1, 11)] for y in range(2, 5)]
print(multiList2)