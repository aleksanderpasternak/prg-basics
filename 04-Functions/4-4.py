###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    absolute = abs(number)
    numstr = str(absolute)
    i = 0
    n = len(numstr)
    total = 0
    while n > 0:
        add = int(numstr[i])
        total += add
        i += 1
        n -= 1
    return total

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')

