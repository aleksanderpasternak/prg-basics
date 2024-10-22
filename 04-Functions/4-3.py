###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
import math
def triangle_area(a,b,c):
    s = 0.5 * (a+ b + c)
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

triangle1 = triangle_area(3,4,5)
triangle2 = triangle_area(5,12,13)
triangle3 = triangle_area(7,24,25)
print('The area of ​​a triangle with sides 3, 4, 5 is ', triangle1)
print('The area of ​​a triangle with sides 5, 12, 13 is ', triangle2)
print('The area of ​​a triangle with sides 7, 24, 25 is ', triangle3)