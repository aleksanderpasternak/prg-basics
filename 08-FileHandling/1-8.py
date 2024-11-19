with open('pets.txt','r') as file:
    content=file.read()
words=content.split()
total=0
for word in words:
    total+=1
print(total)