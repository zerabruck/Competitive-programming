# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root1, root2):
        if not root1:
            return True
        children = []
        if root1.right:
            children.append(root1.right)
        if root1.left:
            children.append(root1.left)

        if not children and not root2.left and  not root2.right:
            return True
        if not children:
            return False
        left = True
        
        if root2.left and  root2.left.val == children[0].val:
            left = self.dfs(root2.left, children[0])
            children.pop(0)

        elif root2.left and root2.left.val == children[-1].val:
            left = self.dfs(root2.left, children[-1])
            children.pop(-1)
        elif root2.left:
            return False
        if len(children) == 2:
            return False
        right = True
        if root2.right and not children:
            return False
        if root2.right and root2.right.val == children[0].val:
            right = self.dfs(root2.right, children[0])
            children.pop()
        if children:
            return False

        return right and left     

    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True

        if not root1 or not root2:
            return False
        if root1.val == root2.val:
            return self.dfs(root1, root2)
        else:
            return False
