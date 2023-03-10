# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        self.node_ava( root)
        return self.count

    def node_ava(self , root):
        if not root:
            return (0 , 0)

        left = self.node_ava( root.left )
        right = self.node_ava( root.right )

        sums = left[0] + right[0] + root.val
        counts = left[1] + right[1] + 1

        if sums // counts == root.val:
            self.count += 1

        return (sums , counts) 
