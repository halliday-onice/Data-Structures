#how can I decompose a number ??
test = 123
test2 = 1000
res1 = test % 10
res2 = (test % 100) // 10
res3 = (test // 100) % 10
print("res1", res1)
print("res2", res2)
print("res3", res3)

roman_dict = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7:'VII', 8:'VIII',
              9: 'IX', 10: 'X', 40: 'XL', 50:'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
roman_dict.items()
print("roman items", roman_dict.items())
print("roman keys", roman_dict.keys())
print("roman values", roman_dict.values())
numbers = [ 75, 99 , 100 , 50]
numbers1 = [ 75,50]
def romanizer(numbers):
      for i in range(numbers):
            if i == 1:
                  print("I")
            elif i  % 10 == 0:
                  print("i: ", i)

#ones_digit = number % 10
#tens_digit = (number // 10) % 10
#hundreds_digit = (number // 100) % 10

#print(ones_digit)     # Output will be 3
#print(tens_digit)     # Output will be 2
#print(hundreds_digit) # Output will be 1