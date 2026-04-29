from collections import deque


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = BinaryTreeNode(value)
        else:
            self._insert_bst(self.root, value)

    def _insert_bst(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = BinaryTreeNode(value)
            else:
                self._insert_bst(node.left, value)
        else:
            if node.right is None:
                node.right = BinaryTreeNode(value)
            else:
                self._insert_bst(node.right, value)

    def get_leaves(self):
        return self._collect_leaves(self.root)

    def _collect_leaves(self, node):
        if node is None:
            return []
        if node.left is None and node.right is None:
            return [node.value]
        return self._collect_leaves(node.left) + self._collect_leaves(node.right)

    def is_avl(self):
        def height_and_balance(node):
            if node is None:
                return 0
            left_h = height_and_balance(node.left)
            if left_h == -1:
                return -1
            right_h = height_and_balance(node.right)
            if right_h == -1:
                return -1
            if abs(left_h - right_h) > 1:
                return -1
            return max(left_h, right_h) + 1

        return height_and_balance(self.root) != -1