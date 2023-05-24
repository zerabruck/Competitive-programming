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

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        self.ele = {}
        visited = set()
        emails = {}  
        for row in range(len(accounts)):
            for col in range(1, len(accounts[row])):
                if accounts[row][col] not in emails:
                    emails[accounts[row][col]] = (row,col)
        
        for row in range(len(accounts)):
            self.ele[(row,0)] = (row,0)
            for col in range(1, len(accounts[row])):
                self.ele[(row,col)] = (row,0) 
                if accounts[row][col] in emails:
                    rep = emails[accounts[row][col]]
                    head = self.find((row,0))
                    self.ele[head] = self.find(rep)
                else:
                    visited.add(accounts[row][col])
        groups = {}
        
        for row in range(len(accounts)):
            for col in range(1, len(accounts[row])):
                
                rep = self.find((row,col))
                if rep in groups:
                    groups[rep].add(accounts[row][col])
                else:
                    groups[rep] = set([accounts[row][col]])
        merged = []

        for rep in groups:
            account = [accounts[rep[0]][rep[1]]]
            orderd = sorted(groups[rep])
            for ele in orderd:
                account.append(ele)
            merged.append(account)
        return merged    
