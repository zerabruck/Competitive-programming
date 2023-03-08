# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def order_traversal(self , root , counter , ele):
        if not root:
            return 

        if len(ele) > counter:
            ele[counter].append(root.val)

        else:
            ele.append([root.val])

        self.order_traversal(root.left , counter + 1 , ele)
        self. order_traversal(root.right , counter + 1 , ele)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ele = []
        self.order_traversal(root , 0 , ele)
        return ele
