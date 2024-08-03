# Reverse Polish Notation
# Reverse Polish notation, also referred to as Polish postfix notation is a way of laying out operators and operands.
# When making mathematical expressions, we typically put arithmetic operators (like +, -, *, and /) between operands. 
# For example: 5 + 7 - 3 * 8

# However, in Reverse Polish Notation, the operators come after the operands. For example: 3 1 + 4 *

# The above expression would be evaluated as (3 + 1) * 4 = 16

# The goal of this exercise is to create a function that does the following:

# Given a postfix expression as input, evaluate and return the correct final answer.
# Note: In Python 3, the division operator / is used to perform float division. So for this problem, 
#you should use int() after every division to convert the answer to an integer.

class Node:
    def __init__(self, value) -> None:
        self.value = value  
        self.Next = None

class stack:
    def __init__(self) -> None:
        self.head = None
        self.noOfElement = 0
    
    def push(self, ele):
        temp = Node(ele)
        if self.head is None:
            self.head = temp
        else:
            temp.Next = self.head
            self.head = temp
        self.noOfElement += 1
    
    def pop(self):
        if self.isEmpty() is None:
            return None
        else:
            temp = self.head.value
            self.head = self.head.Next
        self.noOfElement -= 1
        return temp
    
    def isEmpty(self):
        return self.noOfElement == 0 
    
    def top(self):
        if self.isEmpty():
            return None
        return self.head.value
        
    def size(self):
        return self.noOfElement