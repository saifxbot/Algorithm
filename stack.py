stack = []        # A simple stack implementation using a list in Python

# push
stack.append(10)
stack.append(20)
stack.append(30)

print(stack)      # output: [10, 20, 30]

# pop
top = stack.pop() # removes the last element (top of the stack)
print(top)        # output: 30
print(stack)      # output: [10, 20]
