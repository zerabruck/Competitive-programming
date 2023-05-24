class Solution:
    def find(self, node):
        parent = self.ele[node]
        while parent != self.ele[parent]:
            parent = self.ele[parent]
        while node != self.ele[parent]:
            temp = self.ele[node]
            self.ele[node] = parent
            node = temp
        return parent
    
    def union(self, node1, node2):
        node1_rep = self.find(node1)
        node2_rep = self.find(node2)
        if node1_rep != node2_rep:
            if self.size[node1_rep] < self.size[node2_rep]:
                node1_rep, node2_rep = node2_rep, node1_rep
            self.size[node1_rep] += self.size[node2_rep]
            self.ele[node2_rep] = node1_rep
        

    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        self.ele = {i:i for i in range(len(source))}
        self.size = [1] * len(source)
        groups = {}
        for first, second in allowedSwaps:
            self.union(first, second)
        for ele in self.ele:
            rep = self.find(self.ele[ele])
            if rep in groups:
                groups[rep][0].append(source[ele])
                groups[rep][1].append(target[ele])
            else:
                groups[rep] = [[source[ele]], [target[ele]]]
        count = 0
        for i in groups:
            groups[i][0].sort()
            groups[i][1].sort()
            rep = groups[i]
            first = 0
            second = 0
            while first < len(groups[i][0]) and second < len(groups[i][1]):
                if rep[0][first] > rep[1][second]:
                    second += 1
                elif rep[0][first] < rep[1][second]:
                    first += 1
                else:
                    count += 1
                    first += 1
                    second += 1        

        return  len(source) - count
