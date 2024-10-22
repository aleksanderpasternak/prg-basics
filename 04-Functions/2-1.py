###
# Program for testing built-in functions
#
max_number = max(7,5,6,3,8,2)
print('Max number of 7,5,6,3,8,2 is', max_number)

min_number = min(4,7,2,3,9,8)
print('Min number of 4,7,2,3,9,8 is', min_number)

str_length = len("computer science")
print('The number of characters in "computer science" is', str_length)

letter = input("Enter letter: ")
print('The letter is ', letter)

number = int("20303")
print('The number representing the string "20303" is ', number)

binary = str(bin(304))
print('The binary string representing decimal number 304 is ', binary)

hexadecimal = str(hex(304))
print('The hexadecimal string representing decimal number 304 is ', hexadecimal)

unicode = int(ord("€"))
print('The integer representing the Unicode code of the € sign is', unicode)

absolute = abs(-17)
print('The absolute value of -17 is', absolute)