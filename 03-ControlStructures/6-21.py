amount = int(input("Enter amount in PLN: "))
five = 0
two = 0
one = 0
while amount >= 5:
    amount -= 5
    five += 1
while amount >= 2:
    amount -= 2
    two += 1
while amount >= 1:
    amount -= 1
    one += 1
print(f"5 PLN coins: {five}\n2 PLN coins: {two}\n1 PLN coins: {one}")