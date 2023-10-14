class Solution:
    def __init__(self):
        self.levels = defaultdict(lambda: [float(inf), -float(inf)])
        self.maxWidth = 0

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.maxWidth

    def traverse(self, tree, lvl=0, col=1):
        if not tree:
            return

        self.levels[lvl][0] = min(self.levels[lvl][0], col)
        self.levels[lvl][1] = max(self.levels[lvl][1], col)

        self.maxWidth = max(self.maxWidth, self.levels[lvl][1] - self.levels[lvl][0] + 1)

        self.traverse(tree.left, lvl + 1, (col * 2) - 1)
        self.traverse(tree.right, lvl + 1, col * 2)
