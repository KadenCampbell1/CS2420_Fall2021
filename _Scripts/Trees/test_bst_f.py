'''
Project: pytest BST for Phileas Fogg Project
Author: George Rudolph
Course:  CS 2420 Fall 2020
Date: 1 Nov 2020

Description: 11 test cases to automate grading of a student's BST implementation.
Each BST ADT required operation is tested at least once.
You'll notice that add() and find() are not tested explicitly, except find()
on an empty tree. That's because these functions have to work
in order to build a correct tree at all--if they don't, other tests will fail.

Thinking of dependencies, consider that a test file like this takes
the place of main(), or some other code that exercises the implementation,
so it willl likely have similar dependencies.

Notes:
1. This test depends on the input file "around-the-world-in-80-days-3.txt"
2. This test file is given to students to use for developing their BST code.
3. This is not intended to be exhaustive unit testing, just enough to show
   that their implementation is a good enough implementation of the ADT.
4. These tests ARE intended to automate grading.
5. This version assumes procedural/functional version of the BST.

To run:
Assume you have pytest module installed.
Assume you have the student's bst.py, student's copy of test_bst_f.py and
input file all in same directory.

Open a terminal window in that directory, type 'pytest' as the command and press
enter.
'''
import pytest
from bst import *
from main import Pair, make_tree

def test_create_BST():
    tree = BST()
    assert size(tree) == 0
    assert is_empty(tree)

def test_tree_size():
    tree = make_tree()
    assert size(tree) == 57

def test_tree_height():
    tree = make_tree()
    assert height(tree) == 11

def test_find_empty():
    with pytest.raises(ValueError):
        tree = BST()
        item = find(tree, Pair('A'))

def test_remove_root():
    tree = make_tree()
    remove(tree, Pair('C'))
    pre = preorder(tree)
    assert pre[0] == Pair('D')

def test_remove_internal():
    tree = make_tree()
    pre = preorder(tree)
    i = pre.index(Pair('g'))
    remove(tree, Pair('g'))
    pre = preorder(tree)
    assert pre[i] == Pair('f')

def test_remove_leaf():
    tree = make_tree()
    remove(tree, Pair('z'))
    pre = preorder(tree)
    assert pre[-1] == Pair('w')

def test_preorder():
    tree= make_tree()
    assert preorder(tree)[27] == Pair('R',20)

def test_inorder():
    tree = make_tree()
    assert inorder(tree)[27] == Pair('T',34)

def test_postorder():
    tree = make_tree()
    assert postorder(tree)[27] == Pair('W',13)

def test_rebalance():
    tree = make_tree()
    original_height = height(tree)

    tree2 = rebalance(tree)
    assert not original_height == height(tree2)

def test_code_style():
    from pylint.lint import Run

    results = Run(['bstf.py'], exit=False)
    expected = 8.5
    actual = results.linter.stats['global_note']
    assert actual >= expected
