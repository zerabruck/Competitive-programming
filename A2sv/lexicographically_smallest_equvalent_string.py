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
            if rep_char1 < rep_char2:
                self.ele[rep_char2] = rep_char1
            elif rep_char1 > rep_char2:
                self.ele[rep_char1] = rep_char2


    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        self.ele = {}
        for char in s1:
            self.ele[char] = char
        for char in s2:
            self.ele[char] = char
        for i in range(len(s1)):
            self.union(s1[i], s2[i])
        eq_str = ""
        for char in baseStr:
            if char not in self.ele:
                eq_str += char
            else:
                eq_str += self.find(char)
        return eq_str
