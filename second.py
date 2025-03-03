x = int(input("Enter a number: "))
if x<0:
    x = 0
    print("Negative changed to zero",x)
    
elif x == 0:
    print("Integer is already zero")
    
elif x == 1 :
    print("Integer is one")
    
    
FOR STATEMENTS
list1 = ['cat','dog','elephant']
for w in list1:
    print(w, len(w))
    
  
    sample collection as dictionary 
users = {
    "shivam" : "active",
    "ankit" : "inactive",
    "nitesh": "active",
    }
print(type(users))
for user, status in users .copy().items():
    if status == 'inactive':
        del users[user]
        
active_users = {}

for user, status in users.items():
    if status == "active":
        active_users[user] = status
        
print(users)
print(active_users)


range function

for i in range(0,33,3): 
    print(i)
    
    
a= list(range(0,22,2))
type(a)

a = ["Marry","has","a","little","lamb"]

for i in range(len(a)): #range(s)
    print(i,a[i])
    
    break & continue
    
for num in range(1,10):
        if num == 5:
            continue
        print(num)

for num in range(1,20):
    if num %18 == 0:
        break
    print(num)
