# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def start_node(self,root):
        if not root:
            return

        if root.val in self.delete_set:
            if root.left and root.left.val not in self.delete_set:
                self.soln.append(root.left)
            if root.right and root.right.val not in self.delete_set:
                self.soln.append(root.right)

        self.start_node(root.left)
        self.start_node(root.right)
        if root.left and root.left.val in self.delete_set:
            root.left = None
        if root.right and root.right.val in self.delete_set:
            root.right = None
        

    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        self.delete_set = set(to_delete)
        self.root = root
        self.soln = []
        if self.root.val not in self.delete_set:
            self.soln.append(self.root)
        self.start_node(self.root)
        return self.soln

        