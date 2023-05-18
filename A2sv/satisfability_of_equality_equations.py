class Solution:
    def find(self, node):
        parent = self.ele[node]
        while parent != self.ele[parent]:
            parent = self.ele[parent]
        while node != self.ele[node]:
            temp = self.ele[node]
            self.ele[node] = parent
            node = temp
        return parent

    def union(self, char1, char2):
        rep_char1 = self.find(char1)
        rep_char2 = self.find(char2)
        if rep_char1 != rep_char2:
            if self.size[ord(rep_char1) - ord('a')] >= self.size[ord(rep_char2) - ord('a')]:
                self.size[ord(rep_char1) - ord('a')] += self.size[ord(rep_char2) - ord('a')]
                self.ele[rep_char2] = rep_char1
            elif self.size[ord(rep_char2) - ord('a')] > self.size[ord(rep_char1) - ord('a')]:
                self.size[ord(rep_char2) - ord('a')] += self.size[ord(rep_char1) - ord('a')]
                self.ele[rep_char1] = rep_char2

    def equationsPossible(self, equations: List[str]) -> bool:
        self.ele = { chr(i):chr(i) for i in range(ord('a'), ord('a') + 26)}
        self.size = [1] * 26
        unequals = []
        for eqt in equations:
            if eqt[1] == '!':
                unequals.append((eqt[0], eqt[-1]))
            else:
                self.union(eqt[0], eqt[-1])

        for first, second in unequals:
            if self.find(first) == self.find(second):
                return False
        return True
