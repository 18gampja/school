import random

class Stack:

    def __init__(self, arr):                 # Initializing itself and the array it contains
        self.items = arr

    def push(self, item):
        return self.items.append(item)  # Just a simple push method, adding something on top of the stack

    def pop(self):
        return self.items.pop()         # The pop method to remove and return the value at the top of the stack

    def peakTop(self):
        return self.items[len(self.items)-1]    # Lets you take a sneak peak at the top of the stack
    
    def isEmpty(self):                  # Checks to see if the stack is empty
        if self.items:
            return False
        
        else:
            return True

    def size(self):                     # Returns the size of the stack
        return len(self.items)
    
    def print(self):
        
        newList = []
        
        for i in self.items:
            newList.append(i)
        
        print(newList)
    
    
def genInput(stack1):
    
    i = 0
        
    while i < 10:
        stack1.push(random.randint(0, 50))
        i += 1
        
    return stack1
        
# Part 1: Use two stacks to form a Queue
# I will accomplish this by filling the first stack, which will be first in last out, then
# Moving the contents of that stack to the next one. Logically, this should reverse the order to create a 
# really roundabout and inefficient queue

def sudoQueue(stack1):
    
    stack2 = Stack([])
    i = 0
    limit = stack1.size()
    
    while i < limit:
        
        stack2.push(stack1.pop())
        i += 1
        
    return stack2

def proof(proveStack):
    
    i = 0
    limit = proveStack.size()
    printStack = proveStack
    testList = []
    
    while i < limit:
        
        testList.append(printStack.pop())
        i += 1
        
    return testList
        

# test1 = Stack([])
# genInput(test1)
# print()
# print('The first stack is first in, last out:')
# test1.print()
# print()
# result = sudoQueue(test1)

# print('Since the second stack will ALSO be first in, last out, the order reverses.')
# print('This creates a new stack with the original input as first in, first out, like a queue:')

# result.print()
# print()

# Part 2
# Each check follows the same pattern. We iterate over the string until we find the first delimiter.
# Once found, we push a number representing that type of delimiter ([] = 1, {} = 2, () = 3)
# If it's a left delimiter, we push the number to the stack.
# If it's a right delimiter, we first check to see if the stack is empty. If it is, then it's wrong.
# We then check to see if the top of the stack matches the correct number, if not then it's wrong.
# Finally, we check to see if the real number is either of the other two delimiters, if so then it's wrong.
# If we pass all those checks, we pop the number from the stack.

def checkBalance(sequence):
    
    balanceCheck = Stack([])
    
    for i in sequence:
        
        if i == '[':
            balanceCheck.push(1)
            
        elif i == ']':
            
            if balanceCheck.isEmpty():
                print('Unbalanced')
                return
            
            if balanceCheck.peakTop() != 1:
                
                if balanceCheck.peakTop() == 2 or balanceCheck.peakTop() == 3:
                    print('Unbalanced')
                    return
            
            else:
                balanceCheck.pop()
                
        elif i == '{':
            
            balanceCheck.push(2)
        
        elif i == '}':
            
            if balanceCheck.isEmpty():
                print('Unbalanced')
                return
            
            if balanceCheck.peakTop() != 2:
                
                if balanceCheck.peakTop() == 1 or balanceCheck.peakTop() == 3:
                    print('Unbalanced')
                    return
                    
            else:
                balanceCheck.pop()
            
        elif i == '(':
            
            balanceCheck.push(3)
            
        elif i == ')':
            
            if balanceCheck.isEmpty():
                print('Unbalanced')
                return
            
            if balanceCheck.peakTop() != 3:
                
                if balanceCheck.pop() != 1 and balanceCheck.pop() != 2:
                    print('Unbalanced')
                    return
                    
            else:
                balanceCheck.pop()
                
    if balanceCheck.isEmpty():
        print('Balanced')
    
    else:
        print('Unbalanced')
                
test1 = 'test([])'
test2 = 'test(])'
test3 = 'test([{}])'
test4 = 'test({{}}[[]])'
test5 = 'test)'
test6 = 'test(test{test[test]})'

checkBalance(test1)
# checkBalance(test2)
# checkBalance(test3)
# checkBalance(test4)
# checkBalance(test5)
# checkBalance(test6)