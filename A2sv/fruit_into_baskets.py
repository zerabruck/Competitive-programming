class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_types = {}
        left = 0
        max_fruits = 0
        for right in range(len(fruits)):
            if fruits[right] not in fruit_types:
                fruit_types[fruits[right]] = 1

            else:
                fruit_types[fruits[right]] += 1

            if len(fruit_types) > 2:
                while len(fruit_types) > 2:
                    fruit_types[fruits[left]] -= 1
                    if fruit_types[fruits[left]] == 0 :
                        del fruit_types[fruits[left]]

                    left += 1
            max_fruits = max(max_fruits,right - left + 1 )

        return max_fruits
