from collections import defaultdict,Counter
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        recipe_indegree = Counter(recipes)
        foods = defaultdict(list)
        for index, ingredient in enumerate(ingredients):
            recipe = recipes[index]
            for ele in ingredient:
                foods[ele].append(recipe)
                recipe_indegree[recipe] += 1

        quee = deque(supplies)
        meals = []
        while quee:
            ing = quee.popleft()
            if ing in recipe_indegree and recipe_indegree[ing] == 1:
                meals.append(ing)

            for nebor in foods[ing]:
                if nebor in recipe_indegree:
                    recipe_indegree[nebor] -= 1
                
                if nebor in recipe_indegree and recipe_indegree[nebor] == 1:
                    quee.append(nebor)
        return meals
