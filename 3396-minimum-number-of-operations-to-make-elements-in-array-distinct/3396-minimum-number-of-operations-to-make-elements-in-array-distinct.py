class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i * 3 < n:
            s = set()
            for j in range(i * 3, n):
                if nums[j] not in s:
                    s.add(nums[j])
                else:
                    break
            else:
                return i
            i += 1
        return i
            
        
        

