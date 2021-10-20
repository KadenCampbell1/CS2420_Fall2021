"""The Stack class creates a linked list object.

Functions:
push(item) -- places item onto the top of the Stack object.
pop() -- removes and returns the top item in the Stack.
top() -- returns the top item of the Stack without removing it.
size() -- returns the number of items on the Stack.
clear() -- empties the Stack.
__iter__() -- points to the next object and yields the objects in Stack()
"""
from stack_object import StackObject


class Stack:
    """Creates Stack() with variables: head, cursor"""
    def __init__(self):
        """initiates object with variables: head, cursor set to None"""
        self.head = None
        self.cursor = None

    def push(self, item):
        """push(item) -- places item on top of Stack()

        arguments:
        item -- type Any
        """
        obj = StackObject(item)
        obj.set_next(self.head)
        self.head = obj

    def pop(self):
        """removes and returns the top item in Stack()"""
        if self.head is None:
            raise IndexError
        obj = self.head
        self.head = obj.get_next()
        return obj

    def top(self):
        """returns the top item in Stack() without removing the top"""
        if self.head is None:
            raise IndexError
        return self.head

    def size(self):
        """returns the number of objects in Stack() as int"""
        count = 0
        for i in self:
            count += 1
        return count

    def clear(self):
        """removes all objects in Stack()"""
        self.head = None

    def __str__(self):
        """returns string of Stack

        listed as f"{node}\n"
        """
        nodes = ""
        for node in self:
            nodes += f"{str(node)}\n"
        return nodes

    def __iter__(self):
        """points to the next object and yields the objects in Stack()"""
        node = self.head
        while node is not None:
            yield node
            node = node.next
