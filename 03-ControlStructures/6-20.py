import math

dec = int(input("Decimal number: "))

while dec > 0:
    rem = dec % 2
    dec = math.floor(dec / 2) 
    print(rem, end="")


