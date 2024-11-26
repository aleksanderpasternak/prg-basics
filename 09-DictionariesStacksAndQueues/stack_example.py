import queue

"""
A stack is a linear data structure that follows
the Last In, First Out (LIFO) principle.
This means the last element added to the stack
is the first one to be removed. Think of a stack
as a pile of plates — the last plate you place
on the top is the first one you'll take off.
"""

# creates a stack
cards = queue.LifoQueue()

# adds elements to the top of the stack
cards.put(2)    
cards.put(3)  
cards.put(7)     
cards.put(4)
cards.put(1)
cards.put(9)
cards.put(8)

## prints number of elements of the stack
print('Number of stack elements:', cards.qsize())
i=2
sum1=0
while i>0:
    sum1+=cards.get()
    i-=1
print('Sum of last two numbers:', sum1)
sum=0
# removes and prints elements from the top of the stack
while not cards.empty():
    sum += cards.get()

print('Sum:', sum)
"""
Note the order of the printed elements.
The last added element is printed first.
"""
