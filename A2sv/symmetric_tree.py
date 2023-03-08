# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def symmetric(self , left , right):
        if not left and not right :
            return True

        elif not left or not right:
            return False

        val1 = self.symmetric(left.left , right.right )
        val2 = self.symmetric(left.right , right.left)

        return val1 and val2 and left.val == right.val

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left = root 
        right = root
        return self.symmetric(left , right )
