#Check no is prime or not
num=int(input("Enter a number:"))
r=1
for i in range(2,num):
    r=num%i
    if(r==0):
        break
if(r!=0):
    print("No is prime")
else:
    print("No is not prime")