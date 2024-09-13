class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        answer = [0] * len(queries)
        prefix = [0] * len(arr)
        prefix[0] = arr[0]
        for i in range(1, len(arr)):
            prefix[i] = prefix[i - 1] ^ arr[i]

        for idx, (left, right) in enumerate(queries):
            if left == 0:
                answer[idx] = prefix[right]
            else:
                answer[idx] = prefix[right] ^ prefix[left - 1]
        return answer