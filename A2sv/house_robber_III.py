# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if root.val < 0:
            return -(root.val)
        value = 0
        if root.left:
            value += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            value += self.rob(root.right.left) + self.rob(root.right.right)

        children_val = self.rob(root.left) + self.rob(root.right)
        value += root.val
        max_home =  max(value, children_val)
        root.val = -(max_home)
        return max_home  
