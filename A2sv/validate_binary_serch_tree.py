class Solution:
    def inOrderT(self,root , ele):
        if not root:
            return 

        self.inOrderT(root.left , ele)
        # print(root.val)
        ele.append(root.val)
        self.inOrderT(root.right , ele)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ele = []
        
        self.inOrderT(root , ele)
        sets = set(ele)
        if len(sets) != len(ele) :
            return False
        curr = sorted(ele)
        # print(curr)
        # print(ele)
        return curr == ele
