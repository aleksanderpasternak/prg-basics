import queue
n=13
stack=queue.LifoQueue()
number=""
while n/2>=1:
    stack.put(n%2)
    n/=2
while not stack.empty():
    number+=stack.get
print(number)

