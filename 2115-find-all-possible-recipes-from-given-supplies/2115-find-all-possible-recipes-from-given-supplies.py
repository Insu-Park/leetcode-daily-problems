class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        answer = []        
        recipes_ingredients = deque([pair for pair in zip(recipes, ingredients)])
        count = 0
        while count < len(recipes_ingredients):
            recipe, ingredient = recipes_ingredients.popleft()
            for i in ingredient:
                if i not in supplies:
                    count += 1
                    recipes_ingredients.append((recipe, ingredient))
                    break
            else:
                count = 0
                supplies.append(recipe)
                answer.append(recipe)
        
        return answer
