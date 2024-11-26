stock = {
'Laptop': 15,
'Desktop PC': 10,
'Monitor': 25,
'Keyboard': 50,
'Mouse': 60,
'External Hard Drive': 30,
'Printer': 12,
'Router': 20,
'USB Flash Drive': 100,
'Graphics Card': 8
}
total=0
for item,amount in stock.items():
    print(f'{item}: {amount}')
    total+=amount
print(f'Total amount: {total}')
