class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix = [0]  # 누적 합 배열
        for num in nums:
            prefix.append(prefix[-1] + num)
        
        min_length = float('inf')  # 최소 길이 초기화
        dq = deque()  # Deque를 사용해 유효한 인덱스 관리
        
        for i in range(len(prefix)):
            # 조건을 만족하면 deque에서 pop하고 최소 길이 갱신
            while dq and prefix[i] - prefix[dq[0]] >= k:
                min_length = min(min_length, i - dq.popleft())
            
            # Deque에 있는 이전 값이 현재 prefix보다 크면 제거
            while dq and prefix[dq[-1]] >= prefix[i]:
                dq.pop()
            
            # 현재 인덱스 추가
            dq.append(i)
        
        return min_length if min_length != float('inf') else -1