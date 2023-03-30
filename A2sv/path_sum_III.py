# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pre_order(self, node , pre_val , targetsum):
        if not node:
            return

        curr_val = pre_val + node.val
        if curr_val - targetsum in self.dict:
            self.count += self.dict[curr_val - targetsum]
        if curr_val in self.dict:
            self.dict[curr_val] += 1
        else:
            self.dict[curr_val] = 1
        self.pre_order(node.left , curr_val , targetsum)
        self.pre_order(node.right , curr_val , targetsum)
        self.dict[curr_val] -= 1
        if self.dict[curr_val] == 0:
            del self.dict[curr_val]
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0
        self.dict = {0:1}
        self.pre_order(root , 0 , targetSum)
        return self.count
