"""Design an advanced calculator using math module Features required - 
power, square root, trigonometry"""
import math
print("----------ADVANCED CALCULATOR-----------")
while True:
    print("""Enter The Following Code For Performing Mathematical Calculations:
                 \n 1=Power 
                 \n 2=Square Root 
                 \n 3=Trigonometry
                 \n 4=Exit""")
    ch=int(input("Enter Choice:"))
    if ch==1:
        s=int(input("Enter The Value For Sqaure Root:"))
        print(f"Square Root Of {s} is {math.sqrt(s)}")
    elif ch==2:
        a=int(input("Enter The Base Value:"))
        b=int(input("Enter The Power Value:"))
        print(f"Power {a} base {b} is:{math.pow(a,b)}")
    elif ch==3:
        d=int(input("Enter The Degree:"))
        print(f"""sin{d}={math.sin(d)}
              \n cos{d}={math.cos(d)}
               \n tan{d}={math.tan(d)} """)
    elif ch==4:
        break
    else:
        print("Invalid Choice")
        