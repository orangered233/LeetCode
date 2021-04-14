"""
Background

Algorithm Inorder(tree)
   1. Traverse the left subtree, i.e., call Inorder(left-subtree)
   2. Visit the root.
   3. Traverse the right subtree, i.e., call Inorder(right-subtree)
   **TODO: Can use a stack**

Algorithm Preorder(tree)
   1. Visit the root.
   2. Traverse the left subtree, i.e., call Preorder(left-subtree)
   3. Traverse the right subtree, i.e., call Preorder(right-subtree)

Algorithm Postorder(tree)
   1. Traverse the left subtree, i.e., call Postorder(left-subtree)
   2. Traverse the right subtree, i.e., call Postorder(right-subtree)
   3. Visit the root.
"""

"""
Notes: 
It's known that inorder traversal of BST is an array sorted in the ascending order. 
"""
from typing import List

class Node:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.data = val


def binary_insert(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.l_child is None:
                root.l_child = node
            else:
                binary_insert(root.l_child, node)
        else:
            if root.r_child is None:
                root.r_child = node
            else:
                binary_insert(root.r_child, node)


"""
Trivial Solution:
1. First, in order traverse the tree and get the (almost) sorted list
2. Identify two swapped values in the list
3. Traverse the tree again to swap back
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = self.in_order_traverse(root)
        print(f'nodes: {nodes}')
        self.first_val, self.second_val = self.find_swap(nodes)
        print(f'self.first_val: {self.first_val}')
        print(f'self.second_val: {self.second_val}')
        self.dfs(root)

    def dfs(self, root: TreeNode):
        if root is None:
            return
        if root.val == self.first_val:
            root.val = self.second_val
        elif root.val == self.second_val:
            root.val = self.first_val
        else:
            pass
        self.dfs(root.left)
        self.dfs(root.right)

    def in_order_traverse(self, root: TreeNode) -> List[int]:
        nodes = [root.val]
        if root.left is None and root.right is None:
            return nodes
        if root.left is not None:
            nodes = self.in_order_traverse(root.left) + nodes
        if root.right is not None:
            nodes = nodes + self.in_order_traverse(root.right)
        return nodes

    def find_swap(self, l: List[int]):
        first_pos = -1
        first_val = None
        second_pos = -1
        second_val = None
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                if first_pos == -1:
                    first_pos = i
                else:
                    second_pos = i + 1
        if second_pos == -1:
            second_pos = first_pos + 1
        first_val = l[first_pos]
        second_val = l[second_pos]
        return first_val, second_val

    def in_order_find_swap(self, root: TreeNode):
        """ Use interative method to traverse and find swap """
        x, y = None, None
        pred = None
        stack = []
        while len(stack) > 0 or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pred and root.val < pred.val:
                y = root
                if x is None:
                    x = pred
                else:
                    pass
            pred = root
            root = root.right
        x.val, y.val = y.val, x.val


"""
The idea of Morris algorithm is to set the temporary link between the node and its predecessor: predecessor.right = root. So one starts from the node, computes its predecessor and verifies if the link is present.

There is no link? Set it and go to the left subtree.

There is a link? Break it and go to the right subtree.

There is one small issue to deal with : what if there is no left child, i.e. there is no left subtree? Then go straightforward to the right subtree.
"""

