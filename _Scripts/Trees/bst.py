"""The BST class creates a Binary Search Tree object.

__init__ arguments:
None

Functions:
set_head(node) -- sets head to node
get_head(): -- returns self.head
set_left(node) -- sets left to node
get_left() -- returns self.left
set_right(node) -- sets right to node
get_right() -- returns self.right
is_empty() -- returns true if empty, false otherwise
size() -- returns the number of nodes in the tree
height() -- returns the length of the path from the root to its deepest leaf
add(node) -- add node to its proper place in the tree and returns modified tree
compare(node, tree) -- recursively compares node to tree and traverses left or right until tree is none
remove(node) -- remove node from the tree and returns modified tree
find(node) -- finds and returns the matched node
inorder() -- returns a list with data nodes in order of inorder traversal
preorder() -- returns a list with data nodes in order of preorder traversal
postorder() -- returns a list with data nodes in order of postorder traversal
rebalance() -- rebalances the tree and returns the modified tree
"""


class BST:
    def __init__(self):
        self.head = None
        self.lyst = []

    def set_head(self, node):
        """sets head to node

        arguments:
        node -- type Any
        """
        self.head = node

    def get_head(self):
        """Returns self.head"""
        return self.head

    def is_empty(self):
        """Returns true if empty, false otherwise."""
        if self.head is None:
            return True
        return False

    def size(self, node="self.head"):
        """Returns the number of nodes in the tree."""
        if isinstance(node, str):
            node = eval(node)
        if node is None:
            return 0
        return 1 + self.size(node.get_left()) + self.size(node.get_right())

    def height(self, node="self.head"):
        """Returns the length of the path from the root to its deepest leaf."""
        if isinstance(node, str):
            node = eval(node)
        if node is None:
            return 0

        left_height = self.height(node.get_left())
        right_height = self.height(node.get_right())

        return 1 + max(left_height, right_height)

    def add(self, node):
        """Add node to its proper place in the tree and returns modified tree.

        arguments:
        node -- type Any
        """
        if self.is_empty():
            self.set_head(node)
        else:
            self.compare(node, self.get_head())
        return self

    def compare(self, node, tree):
        """recursively compares node to tree and traverses left or right until tree is none

        arguments:
        node -- type Any
        tree -- type Any
        """
        if node == tree:
            tree.count += 1
        elif node < tree:
            if tree.get_left() is None:
                tree.set_left(node)
            else:
                self.compare(node, tree.get_left())
        elif node > tree:
            if tree.get_right() is None:
                tree.set_right(node)
            else:
                self.compare(node, tree.get_right())
        else:
            print(f"node{node}, tree{tree}")

    def remove(self, node):
        """Remove node from the tree and returns modified tree.

        arguments:
        node -- type Any
        """
        pass

    def find(self, node, travel="self.head"):
        """Finds and returns the matched node.

        arguments:
        node -- type Any
        """
        if isinstance(travel, str):
            travel = eval(travel)
        if self.head is None:
            raise ValueError("Node not in tree")
        if travel is None:
            return None
        if node == travel:
            return node
        else:
            left = self.find(node, travel.get_left())
            right = self.find(node, travel.get_right())
            if left is not None:
                return left
            elif right is not None:
                return right
            elif left and right is None:
                raise ValueError("Node not in tree.")
            else:
                return None

    def inorder(self, node="self.head"):
        """Returns a list with data nodes in order of inorder traversal."""
        if isinstance(node, str):
            node = eval(node)
        if node:
            self.lyst.append(self.inorder(node.get_left()))
            self.lyst.append(node)
            self.lyst.append(self.inorder(node.get_right()))
        else:
            return node

    def preorder(self):
        """Returns a list with data nodes in order of preorder traversal."""
        pass

    def postorder(self):
        """Returns a list with data nodes in order of postorder traversal."""
        pass

    def rebalance(self):
        """Rebalances the tree and returns the modified tree."""
        pass

    # def __str__(self):
    #     """returns string of BST as f"{node}"""
    #     return f"{self.node}"
