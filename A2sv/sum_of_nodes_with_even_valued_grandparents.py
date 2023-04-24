# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def grand_children(self , node):
        if not node:
            return
        left = node.left
        right = node.right
        if left:
            left_left = left.left
            left_right = left.right
            if left_left:
                self.children.append(left_left.val)
            if left_right:
                self.children.append(left_right.val)
        if right:
            right_left = right.left
            right_right = right.right
            if right_left:
                self.children.append(right_left.val)
            if right_right:
                self.children.append(right_right.val)
    def dfs(self , node):
        if not node:
            return
        if node.val % 2 == 0:
            self.grand_children(node)
        self.dfs(node.left)
        self.dfs(node.right)

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.children = []
        self.dfs(root)
        return sum(self.children)
