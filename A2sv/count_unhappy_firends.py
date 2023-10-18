class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        ranks = [[0 for _ in range(n)] for _ in range(n)]
        for index in range(len(preferences)):
            count = 1
            for eles in preferences[index]:
                ranks[index][eles] = count 
                count += 1

        pair_dict = {}
        for first, second in pairs:
            pair_dict[first] = second
            pair_dict[second] = first

        unhappy = set()

        for first, second in pairs:
            if ranks[first][second] != 1 and first not in unhappy:
                for other in preferences[first]:
                    if other == second:
                        break
                    if ranks[other][first] < ranks[other][pair_dict[other]]:
                        unhappy.add(first)
                        unhappy.add(other)
            if ranks[second][first] != 1 and second not in unhappy:
                for other in preferences[second]:
                    if other == first:
                        break
                    if ranks[other][second] < ranks[other][pair_dict[other]]:
                        unhappy.add(second)
                        unhappy.add(other)
        return len(unhappy)      
