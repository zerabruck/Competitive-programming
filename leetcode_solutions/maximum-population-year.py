class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        # 100 years
        # [1,0,-1, 0, 1, 0, 0 , 0 ,-1]
        # [1,1, 0, 0, 1, 1, 1, 1, 0 ]
        year = [0] * 101
        const_intial = 1950
        for birth, death in logs:
            year[birth - const_intial] += 1
            year[death - const_intial] -= 1

        pref = [0] * 101
        pref[0] = year[0]
        min_year = 0
        max_pop = pref[0]

        for population in range(1, len(year)):
            pref[population] = pref[population - 1] + year[population]
            if pref[population] > max_pop:
                max_pop = pref[population]
                min_year = population
        return const_intial + min_year


        