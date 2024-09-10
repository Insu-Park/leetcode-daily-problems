# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node and node.next:
            next = node.next
            gcd = math.gcd(node.val, next.val)
            node.next = ListNode(val=gcd, next=next)
            node = node.next.next
        
        return head