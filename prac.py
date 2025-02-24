class Stack:
    def __init__(self):
        # Initialize the stack as an empty list
        self.stack = []

    # Push operation: Adds an element to the stack
    def push(self, element):
        self.stack.append(element)
        print(f"Element {element} pushed to stack.")

    # Pop operation: Removes the element from the top of the stack
    def pop(self):
        if self.is_empty():
            return "Stack is empty, cannot pop."
        else:
            popped_element = self.stack.pop()
            return f"Element {popped_element} popped from stack."

    # Peek operation: Returns the element at the top of the stack without removing it
    def peek(self):
        if self.is_empty():
            return "Stack is empty."
        else:
            return f"Top element is: {self.stack[-1]}"

    # Check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Get the size of the stack
    def size(self):
        return f"Stack size is: {len(self.stack)}"

# Test the stack operations
stack = Stack()

# Perform operations0
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.peek())   # Should show the top element (30)
print(stack.pop())    # Should remove and return the top element (30)
print(stack.size())   # Should show the current size of the stack
print(stack.pop())    # Should remove and return the top element (20)
print(stack.is_empty())  # Should check if stack is empty (False)
print(stack.pop())    # Should remove and return the last element (10)
print(stack.is_empty())  # Should check if stack is empty (True)
