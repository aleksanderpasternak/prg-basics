stock = [(20,5.50),(15,8.30),(37,3.85),(4,11.60)]
value = lambda x: stock[x][0]*stock[x][1]
total = 0
for n in range(0,len(stock)):
    total += value(n)
print(total)