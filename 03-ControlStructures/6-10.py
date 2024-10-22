human_years = float(input("Enter the dog's age in human years: "))
age = 0
while human_years > 0:
    if human_years <= 2:
        age += 10.5
    else:
        age += 4
    human_years -= 1
print(f"The dog's age in dog's years is {age} years.")