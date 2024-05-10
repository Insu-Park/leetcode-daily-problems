class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        l = len(arr)
        arr.sort()
        answer = []
        for i in range(l):
            for j in range(0, i):
                answer.append([arr[j] / arr[i], [arr[j], arr[i]]])

        answer.sort(key=lambda x:x[0])
        return answer[k - 1][1]