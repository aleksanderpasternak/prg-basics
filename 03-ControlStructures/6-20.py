dec = int(input("Decimal number: "))

while dec > 0:
    dec = dec / 2
    remainder = dec % 2
    print(f"{remainder}")
