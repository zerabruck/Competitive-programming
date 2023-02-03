class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        setting = set()
        chemistry = 0
        skill.sort()
        beg = 0
        end = len(skill) - 1
        while(beg <= end ):
            first_val = skill[beg]
            second_val = skill[end]

            chemistry += (first_val * second_val )
            setting.add((first_val + second_val))
            beg += 1
            end -= 1

        if len(setting) == 1:
            return chemistry

        return -1
