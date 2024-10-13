###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#
# read temperature
c = input('Temperature in degrees Celsius: ')
# convert to Fahrenheit
f = (9 / 5) * float(c) + 32 
# convert to Kelvin
k = float(c) + 273.15
# display the values
print(f'Temperature: {c}°C, {round(f,2)}°F, {round(k,2)}K')