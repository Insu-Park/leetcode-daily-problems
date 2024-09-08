# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        node = head
        count = 0
        answer = []
        while node:
            count += 1
            node = node.next

        node = head
        if count < k:
            while node:
                now = node
                node = node.next
                now.next = None
                answer.append(now)
            answer.extend([None] * (k - count))
        
        else:
            a, b = count // k, count % k
            p = [a] * k
            for i in range(b):
                p[i] += 1

            i, idx = 0, 0
            new_head = node
            while node:
                i += 1
                now = node
                node = node.next
                if i == p[idx]:
                    now.next = None
                    answer.append(new_head)
                    new_head = node
                    i = 0
                    idx += 1
        
        return answer