"""

Stack ADT

"""

class Stack:

    """class has given attributes for adt, stack."""

    def __init__(self, size=0):
        self.items = []
        self.stack_size = size

    def push(self, item):
        """inserts item at the top of the stack"""
        self.items.append(item)

    def is_empty(self):
        """checks to see stack is empty"""
        return self.items == []

    def pop(self):
        """removes and returns item at the top of the stack.
        Precondition: the stack is not empty, raises keyError
        Postcondition: the top item is removed from stack."""
        if self.is_empty():
            raise IndexError
        else:
            return self.items.pop()

    def top(self):
        """returns item at the top of the stack.
        Precondition: the stack is not empty."""
        if self.is_empty():
            raise IndexError
        else:
            return self.items[len(self.items) - 1]

    def size(self):
        """returns the number of items in stack"""
        return len(self.items)

    def clear(self):
        """makes self become empty"""
        self.items = []
    