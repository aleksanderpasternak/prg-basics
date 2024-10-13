#
# The speed of vehicles on a highway in Poland must be between 40 and 140 km/h. Write a program that checks whether the vehicle speed entered from the keyboard is correct. Sample result:
# Enter vehicle speed: 158
# Speed is valid: False
#
speed = input('Enter vehicle speed: ')
correct = 40 <= int(speed) <= 140
print(f'Speed is valid: {correct}')