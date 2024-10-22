current = int(input("Current product price: "))
previous = int(input("Previous product price: "))
discount = (1 - current / previous) * 100
if discount >= 10:
    print(f"Buy the product!!\nProduct price reduced by {round(discount)}%")