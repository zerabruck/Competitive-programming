# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        head = TreeNode(preorder[0])
        stack = [head]
        for order in preorder[1:] :
            new = TreeNode(order)
            if stack[-1].val > new.val :
                stack[-1].left = new
                stack.append(new)

            else:
                poped = stack[-1]
                while stack and stack[-1].val < new.val:
                    poped = stack.pop()

                poped.right = new
                stack.append(new)
        return head
