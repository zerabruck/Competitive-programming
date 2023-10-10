# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, sums, path):
        if not node:
            return []
        if not node.left and not node.right:
            if sums + node.val == self.targetSum:
                paths = [path.copy()]
                paths[0].append(node.val)
                return paths
            else:
                return []
     
        path.append(node.val)
        left_path = self.dfs(node.left, sums + node.val, path)
        right_path = self.dfs(node.right, sums + node.val, path)
        path.pop()
        return [*left_path, *right_path]
   
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.targetSum = targetSum
        result = self.dfs(root, 0, [])
        return result       
