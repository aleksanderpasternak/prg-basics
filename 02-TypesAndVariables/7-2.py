###
# A program that checks whether the password length
# read from the keyboard is correct.
#
password = input('Enter password: ')
password_ok = len(password) >= int(8)
print(f'Password length is valid: {password_ok}')