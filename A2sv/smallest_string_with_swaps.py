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
        if self.rank[rep_char1] < self.rank[rep_char2]:
            rep_char1, rep_char2 = rep_char2, rep_char1
        self.rank[rep_char1] += self.rank[rep_char2]
        self.ele[rep_char1] = rep_char2


    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        self.ele = { i : i for i in range(len(s))}
        self.rank = [1] * len(s)
        self.reps = {}

        for first, second in pairs:
            self.union(first, second)

        for key, value in self.ele.items():
            rep = self.find(value)
            if rep not in self.reps:
                self.reps[rep] =[[s[key]],0]

            else:
                self.reps[rep][0].append(s[key])
        for i in self.reps:
            self.reps[i][0].sort()
        eq_str = ""
        for char in range(len(s)):
            key = self.find(char)
            orderd_val = self.reps[key][0][self.reps[key][1]]
            self.reps[key][1] += 1
            eq_str += orderd_val
        return eq_str
