ean = str(input("Enter EAN-13 article number: "))
check = ean[0:3]
if len(ean) == 13:
    print("Article number is correct")
elif len(ean) != 13:
    print("Article number is incorrect")
if check == "590":
    print("Article manufactured in Poland")