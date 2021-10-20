"""The Stack class creates a linked list object.

Functions:
push(item) -- places item onto the top of the Stack object.
pop([obj]) -- removes and returns the top item in the Stack.
top([obj]) -- returns the top item of the Stack without removing it.
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

    def pop(self, obj_type=False):
        """removes and returns the top item in Stack()

        if obj is false it returns the value.
        true it returns the object
        arguments:
        obj -- type bool
        """
        if self.head is None:
            raise IndexError
        obj = self.head
        self.head = obj.get_next()
        if obj_type is False:
            return obj.get_item()
        else:
            return obj

    def top(self, obj_type=False):
        """returns the top item in Stack() without removing the top

        if obj is false it returns the value.
        true it returns the object
        arguments:
        obj -- type bool
        """
        if self.head is None:
            raise IndexError
        if obj_type is False:
            return self.head.get_item()
        else:
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
