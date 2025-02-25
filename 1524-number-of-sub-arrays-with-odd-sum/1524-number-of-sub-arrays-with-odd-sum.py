class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        answer = 0
        odd_sum = even_sum = acc = 0
        for i in range(n):
            acc += arr[i]
            if acc % 2 == 0:
                even_sum += 1
                answer += odd_sum
            else:
                odd_sum += 1
                answer += even_sum + 1
        
        answer %= 10 ** 9 + 7
        return answer