###
# Checks the correctness of username and password
#
import re

# read username and password from keyboard
username = input('Username: ')
password = input('Password: ')

# pattern (criteria) for username and password
username_pattern = '.{6,}{^\W}'
password_pattern = '.{8,}{\w}{\W}'

# check if username and password are ok
username_match = re.match(username_pattern,username)
...

# print results
if ... and ...:
   print(...)
else:
   ... 