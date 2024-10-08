###
# Enter price: 24.72
# Enter discount %: 15
# Price with discount: 21.01
# Reduction: 3.71
#
price = input("Enter price: ")
discount = input("Enter discount %: ")
price_with_discount = float(price) * ( 1 - float(discount)/ 100 )
reduction = float(price) - price_with_discount
print(f"Price: {price}\nDiscount: {discount}\nPrice with discount: {price_with_discount}\nReduction: {reduction}")