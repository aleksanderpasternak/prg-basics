import queue

#Use a stack. Read the next characters of the expression. 
#Skip all but the brackets. If it is an opening bracket, put it on the stack. 
#If it is a closing bracket, get the item from the stack and compare whether 
#it is a matching opening bracket.

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

def brackets_ok(expression):
    stack=queue.LifoQueue()
    error=0
    open=0
    close=0
    for  char in expression:
        if char == '(' or char == '[' or char == '{':
            stack.put(char)
            open+=1
        elif char ==')':
            if stack.get()!='(':
                error+=1
            close+=1
        elif char==']':
            if stack.get()!='[':
                error+=1
            close+=1
        elif char=='}':
            if stack.get()!='{':
                error+=1
            close+=1
    if close!=open:
        error+=1
    return error==0#True if brackets in expression are ok of False otherwise

if brackets_ok(expression1):
   print('Brackets ok')
else:
   print('Brackets not correct')

if brackets_ok(expression2):
   print('Brackets ok')
else:
   print('Brackets not correct')

if brackets_ok(expression3):
   print('Brackets ok')
else:
   print('Brackets not correct')