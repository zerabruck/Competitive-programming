# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.paths = []
        self.path_finder("" , root)
        return self.paths

    def path_finder (self , visited , root ):
        if not root.left and not root.right :
            self.paths.append(visited + f"{root.val}")
            return
        if root.right:
            self.path_finder( visited + f"{root.val}->" , root.right )

        if root.left:
            self.path_finder( visited + f"{root.val}->" , root.left )
