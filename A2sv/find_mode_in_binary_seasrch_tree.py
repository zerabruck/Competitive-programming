# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.dicto = {}
        self.traverser(root)
        maximo = max(self.dicto.values())

        mode = []
        for key , value in self.dicto.items() :
            if value == maximo :
                mode.append(key)

        return mode

    def traverser(self , root ):
        if not root:
            return 
        
        if root.val in self.dicto:
            self.dicto[root.val] += 1

        else:
            self.dicto[root.val] = 1

        self.traverser(root.left)
        self.traverser(root.right)      
