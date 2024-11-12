categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]
i=0
while i < len(categories):
    categories[i]=categories[i]+"."+str(i)
    i+=1
n=0
while n < len(expenses):
    expenses[n]=expenses[n]+n/10
    n+=1
expenses.sort(reverse=True)
id=str(expenses[0])[-1]
cat=0
for item in categories:
    if item[-1]==id:
        cat=item
print(str(cat)[:-2],":",str(expenses[0])[:-2])
