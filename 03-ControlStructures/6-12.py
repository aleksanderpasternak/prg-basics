number = int(input("Number of products purchased: "))
price = int(input("Product price: "))
final = 0
if number >= 2:
    final = price * 2 + (price * (number - 2) * 0.75)
else:
    final = price * number
print(f"Amount to pay: {final}")