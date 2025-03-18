class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        answer = 1
        square_of_two = [2 ** i for i in range(31, -1, -1)]
        used_binary = []
        subarray_binary = set()
        for num in nums:
            new_binary = set()
            for i, t in enumerate(square_of_two):
                if num >= t:
                    num -= t
                    new_binary.add(i)

            
            used_binary.append(new_binary)
        start, end = 0, 0

        while end < len(nums):
            if len(subarray_binary & used_binary[end]) > 0:
                # print("check", subarray_binary, used_binary[end])
                answer = max(answer, end - start)
                while len(subarray_binary & used_binary[end]) > 0:
                    # print("holy", subarray_binary, used_binary[start], nums[start])
                    subarray_binary -= used_binary[start]
                    start += 1
            
            subarray_binary |= used_binary[end]
            # print(start, end, nums[start], nums[end], subarray_binary, used_binary[end])

            end += 1

        answer = max(answer, end - start)
        return answer