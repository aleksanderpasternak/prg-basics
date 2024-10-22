number = 0
while number < 30:
    number += 1
    if number % 3 == 0 and number % 5 == 0:
        print("BINGO", end=" ")
    elif number % 3 == 0:
        print("THREE", end=" ")
    elif number % 5 == 0:
        print("FIVE", end=" ")
    else:
        print(number, end=" ")
    