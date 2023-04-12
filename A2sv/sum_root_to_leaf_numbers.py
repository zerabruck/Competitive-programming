# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self , node , visited):
        if  not node:   
            return
        if node.left == None and node.right == None:
            visited += str(node.val)
            self.routes.append(int(visited))
            return

        visited += str(node.val)
        self.dfs(node.right , visited)
        self.dfs(node.left , visited)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.routes = []     
        self.dfs(root , '')      
        sums = sum(self.routes)
        return sums
