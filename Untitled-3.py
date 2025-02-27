def is_palindrome(number):
 
  if not isinstance(number, int) or number < 0:
      return False

  num_str = str(number)

  reversed_str = num_str[::-1]

  return num_str == reversed_str


print(is_palindrome(121))   
print(is_palindrome(123))   

