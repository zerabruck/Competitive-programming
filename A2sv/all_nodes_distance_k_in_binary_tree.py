from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def populate(self, node):
        if node.left:
            self.adj_list[node.val].append(node.left.val)
            self.adj_list[node.left.val].append(node.val)
            self.populate(node.left)
        if node.right:
            self.adj_list[node.val].append(node.right.val)
            self.adj_list[node.right.val].append(node.val)
            self.populate(node.right)


    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.adj_list = defaultdict(list)
        res = []
        self.populate(root)

        quee = deque([(target.val, 0)])
        visited = set([target.val])
        if k == 0:
            return [target.val]
        while quee:
            val = quee.popleft()
            if val[1] == k:
                res.append(val[0])

            for child in self.adj_list[val[0]]:
                if child not in visited:
                    visited.add(val[0])
                    quee.append((child, val[1] + 1))

        return res
