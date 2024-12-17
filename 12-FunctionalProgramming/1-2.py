# takes two numbers from keyboard
n1 = input('First number: ')
n2 = input('Second number: ')

# define an anonymous function
mean = lambda x,y: (float(x)+float(y))/2


# calculates arightmtic mean and print result
result = mean(n1,n2)
print(f"The arithmetic mean of {n1} and {n2} is {result}")