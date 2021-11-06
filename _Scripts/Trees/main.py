"""
Project 5: Trees
Author: Kaden Campbell
Course: CS2470
Date: 10/26/2021

Description:

Lessons Learned:

"""
from pathlib import Path
from string import whitespace, punctuation
from bst import BST


class Pair:
    """ Encapsulate letter,count pair as a single entity.

    Relational methods make this object comparable
    using built-in operators.
    """

    def __init__(self, letter, count=1):
        self.letter = letter
        self.count = count
        self.left = None
        self.right = None

    def set_left(self, node):
        """sets left to node

        arguments:
        node -- type Any
        """
        self.left = node

    def get_left(self):
        """returns self.left"""
        return self.left

    def set_right(self, node):
        """sets right to node

        arguments:
        node -- type Any
        """
        self.right = node

    def get_right(self):
        """returns self.right"""
        return self.right

    def __eq__(self, other):
        return self.letter == other.letter

    def __hash__(self):
        return hash(self.letter)

    def __ne__(self, other):
        return self.letter != other.letter

    def __lt__(self, other):
        return self.letter < other.letter

    def __le__(self, other):
        return self.letter <= other.letter

    def __gt__(self, other):
        return self.letter > other.letter

    def __ge__(self, other):
        return self.letter >= other.letter

    def __repr__(self):
        return f'({self.letter}, {self.count})'

    def __str__(self):
        return f'({self.letter}, {self.count})'


def make_tree():
    """ A helper function to build the tree.

    The test code depends on this function being available from main.
    :param: None
    :returns: A binary search tree
    """

    bst = BST()
    with open("around-the-world-in-80-days-3.txt") as DATA_FILE:
        for x in DATA_FILE:
            for char in x:
                if 48 <= ord(char) <= 57 or 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122:
                    pair = Pair(char)
                    bst.add(pair)

    return bst


def main():
    make_tree()


if __name__ == "__main__":
    main()
