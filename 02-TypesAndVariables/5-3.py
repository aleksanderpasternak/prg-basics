###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = input('a=')
b = input('b=')
c = input('c=')
a_int = int(a)
b_int = int(b)
c_int = int(c)
volume = a_int * b_int * c_int
area = 2 * a_int * b_int + 2 * b_int * c_int + 2 * a_int * c_int
print(f"Volume={volume}, Area={area}")