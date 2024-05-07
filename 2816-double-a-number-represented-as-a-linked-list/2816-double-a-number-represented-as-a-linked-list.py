# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sys.set_int_max_str_digits(100000) 
        node = head
        nodes = []
        while node:
            nodes.append((str)(node.val))
            node = node.next

        nodes = (str)((int)("".join(nodes)) * 2)
        answer = None

        for node in nodes[::-1]:
            answer = ListNode(val=node, next=answer)

        return answer