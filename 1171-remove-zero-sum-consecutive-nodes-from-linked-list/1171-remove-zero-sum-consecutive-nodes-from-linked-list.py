# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        ans = 0
        d = {ans: dummy}
        while head:
            ans += head.val
            d[ans] = head
            head = head.next
        head = dummy
        ans = 0
        while head:
            ans += head.val
            head.next = d[ans].next
            head = head.next
        return dummy.next        