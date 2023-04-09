"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        val = 0
        for child in root.children:
            new_val = self.maxDepth(child)
            val = max(val , new_val)
        val += 1
        return val
