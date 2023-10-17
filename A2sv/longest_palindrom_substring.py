# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def search(self, node, value):
        if not node: 
            return 0
        if node.val == value:
            self.sets.add(node)
            return 1

        left = self.search(node.left, value)
        right = self.search(node.right, value)
        
        if left + right == 1:
            self.sets.add(node)
            return 1
        return 0

    def find(self, node, value):
        if not node: 
            return 0
        if node.val == value:
            if node in self.sets:
                self.common = node
            return 1

        left = self.find(node.left, value)
        right = self.find(node.right, value)
        
        if left and self.common == self.root and node in self.sets:
            self.common = node
            return 0
        
        if right and  self.common == self.root and node in self.sets:
            self.common = node
            return 0
        
        return right + left
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.sets = set()
        self.search(root, p.val)
        self.common = root
        self.root =root
        self.find(root, q.val) 
        return self.common      
