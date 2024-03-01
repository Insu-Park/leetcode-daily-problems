# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def getLinkedListNumber(node, nums):
            if not node:
                return int(nums[::-1])
            else:
                return getLinkedListNumber(node.next, nums + str(node.val))
        
        tmp = str(getLinkedListNumber(l1, "") + getLinkedListNumber(l2, ""))
        answer = [None] * len(tmp)
        answer[0] = ListNode(tmp[0])
        for i in range(1, len(tmp)):
            answer[i] = ListNode(tmp[i], answer[i - 1])  
        return answer[len(tmp) - 1]