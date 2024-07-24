class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        new_nums = [list(str(num)) for num in nums]
        modified = []
        for idx, num in enumerate(new_nums):
            modified.append([nums[idx], int("".join([str(mapping[int(c)]) for c in num]))])

        print(modified)
        return [origin for origin, new in sorted(modified, key=lambda x: x[1])]

            
            