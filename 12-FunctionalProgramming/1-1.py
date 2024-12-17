###
# Calculates arithmetic mean of two integer numbers
#
def mean(x,y):
   r = (float(x)+float(y))/2
   return r

# takes two numbers from keyboard
n1 = input('First number: ')
n2 = input('Second number: ')

# calculates arightmtic mean and print result
result = mean(n1,n2)
print(f'The arithmetic mean of the numbers {n1} and {n2} is {result}')