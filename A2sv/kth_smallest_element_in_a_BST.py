# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallest_helper(self , root , ele , k) -> int:
        
        if not root and len(ele) == 0:
            ele.append(0)
            return 

        elif not root :
            return

        left_val = self.smallest_helper(root.left , ele , k)

        ele[0] += 1
        if ele[0] == k:
            ele.append(root.val)

        self.smallest_helper(root.right , ele , k)


    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ele = []
        self.smallest_helper(root , ele ,k)
        return ele[1]
