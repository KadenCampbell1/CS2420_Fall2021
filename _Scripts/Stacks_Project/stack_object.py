"""The StackObject class creates a StackObject object.

__init__ arguments:
item -- type Any

Functions:
get_item() -- returns self.item
set_next(node) -- sets pointer to node
get_next() -- returns self.next
__str__() -- returns string of StackObject as f"{item}"
"""


class StackObject:
    """Creates a StackObject() with variables: item

    Functions:
    set_next(node) -- sets pointer to node
    get_next() -- returns self.next
    __str__() -- returns string of StackObject as f"{item}"
    """

    def __init__(self, item):
        """inits StackObject object with pointer to None

        arguments:
        item -- type Any
        """
        self.item = item
        self.next = None

    def get_item(self):
        """get_item() -- returns self.item"""
        return self.item

    def set_next(self, node):
        """set_next(node) -- sets pointer to node
        arguments:
        node -- type StackObject()
        """
        self.next = node

    def get_next(self):
        """get_next() -- returns self.next"""
        return self.next

    def __str__(self):
        """returns string of StackObject as f"{item}"""
        return f"{self.item}"
