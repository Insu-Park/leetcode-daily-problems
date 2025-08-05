class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        answer = 0
        for fruit in fruits:
            i = 0
            while i < len(baskets):
                if fruit <= baskets[i]:
                    baskets[i] = 0
                    break
                i += 1
                if i == len(baskets):
                    answer += 1
        
        return answer
            
            



