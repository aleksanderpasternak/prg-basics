###
# Calculation of circle area and circumference 
#

# determine radius and PI values
r = input('Enter radius of the circle: ')
pi = 3.14
# calculate area 
area = pi * int(r) ** 2
# calculate circumference
circumference =  2 * pi * int(r)
# display results
print(f'Radius: {r}\nArea: {area}\nCircumference: {circumference}')