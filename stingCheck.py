# Write a Python program to check if a string contains only digits.

def stringCheck(s=""):
  digits="0123456789"
  for char in s:
    if char in digits:
      print("String contains digits")
      break
  else:
    print("String does not contain digits")
      

a = str(input("Enter the string: "))
stringCheck(a)