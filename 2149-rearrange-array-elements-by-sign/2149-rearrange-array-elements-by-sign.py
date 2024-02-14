class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg, ans = [], [], []
        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)
        
        idx = 0
        while idx != len(pos):
            ans.append(pos[idx])
            ans.append(neg[idx])
            idx += 1
        
        return ans
