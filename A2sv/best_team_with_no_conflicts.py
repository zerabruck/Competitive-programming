class Solution:
    def simulate(self, index, prev_index):
        if index >= len(self.scores):
            return 0
        if (index, prev_index) not in self.dp:
            not_choose = self.simulate(index + 1, prev_index)
            choose = 0
            if prev_index == -1:
                choose = self.scores[index][1] + self.simulate(index + 1, index)
            elif self.scores[index][0] == self.scores[prev_index][0]:
                choose = self.scores[index][1] + self.simulate(index + 1, index)

            elif self.scores[index][1] >= self.scores[prev_index][1]:
                choose = self.scores[index][1] + self.simulate(index + 1, index)

            self.dp[(index, prev_index)] = max(choose, not_choose)
        return self.dp[(index, prev_index)]
            
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        self.dp = {}
        self.scores = [(ages[i], scores[i]) for  i in range(len(scores))]
        self.scores.sort()
        return self.simulate(0, -1)     
