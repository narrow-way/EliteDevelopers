#!/usr/bin/python3

#Python Project (Building a stack)

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty. Cannot pop.")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty. Cannot peek.")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# Create an instance of the stack
my_stack = Stack()

# Push some elements onto the stack
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)

# Perform stack operations
print("Is stack empty?", my_stack.is_empty())
print("Stack size:", my_stack.size())
print("Top element:", my_stack.peek())

popped_item = my_stack.pop()
print("Popped item:", popped_item)

print("Stack size after pop:", my_stack.size())
print("Is stack empty?", my_stack.is_empty())
