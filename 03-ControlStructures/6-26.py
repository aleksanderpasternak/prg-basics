pin = "0805"
enter = input("Enter the PIN code: ")
i = 0
while enter != pin and i < 2:
    print("Incorrect...")
    i += 1
    enter = input("Enter the PIN code: ")
if enter == pin:
    print("OK")
if i >= 2:
    print("Sorry, your payment card has been blocked.")
