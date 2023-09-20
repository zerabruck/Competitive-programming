class Solution:
    def diff(self, str1, str2):
        diff = 0
        for index in range(len(str1)):
            if str1[index] != str2[index]:
                diff += 1
        return diff

    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        que = deque()
        visited = set()
        bank_dicto = {}
        for index in range(len(bank)):
            bank_dicto[index] = bank[index]
        remove = []

        for ele in bank_dicto:
            if self.diff(bank_dicto[ele], startGene) == 1:
                que.append((bank_dicto[ele], 1))
                if bank_dicto[ele] == endGene:
                    return 1
                remove.append(ele)
        for key in remove:
            del bank_dicto[key]

        while que:
            curr = que.popleft()
            curr_arr = curr[0]
            remove = []
            for ele in bank_dicto:
                if self.diff(bank_dicto[ele], curr_arr) == 1:
                    que.append((bank_dicto[ele], curr[1] + 1))
                    if bank_dicto[ele] == endGene:
                        return curr[1] + 1
                    remove.append(ele)
            for key in remove:
                del bank_dicto[key]
        return -1 
