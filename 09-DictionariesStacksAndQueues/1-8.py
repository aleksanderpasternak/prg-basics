price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99

#prints a list of products and their prices before the discount
}
total=0
for item,value in price_list.items():
    print(f'{item}: {value}')
    total+=value
#prints the total value of the products before the discount
print(f'Total:  {round(total,2)}')
#modifies the price list according to the discount (round prices to two decimal places)
print('AFTER DISCOUNT')
for item,value in price_list.items():
    price_list[item]*=0.9
#prints a list of products and their prices after the 10% discount
total=0
for item,value in price_list.items():
    print(f'{item}: {round(value,2)}')
    total+=value
#prints the total value of the products after the discount
print(f'Total:  {round(total,2)}')