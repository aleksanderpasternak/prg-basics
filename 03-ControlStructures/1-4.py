###
# Credit card payment 
#
account_balance = 500
total_payment = input("Total payment: ")

if float(total_payment) < account_balance:
    print('Payment completed')
else:
    print('No funds')