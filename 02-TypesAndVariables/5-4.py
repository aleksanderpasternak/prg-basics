###
# Amount  : 15.84
# VAT 23% :  3.64
#
amount = input("Amount:")
vat = float(amount) * 0.23
rounded_vat = round(vat, 2)
print(f"Amount : {amount}\nVAT 23% : {rounded_vat}")