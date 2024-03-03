# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        self.stack = []
        def dfs(node):
            if not node:
                return
            self.stack.append(node.val)
            dfs(node.next)
        
        dfs(head)
        del self.stack[(-1) * n]
        
        if not self.stack:
            return None

        answer = None

        for s in self.stack[::-1]:
            answer = ListNode(val=s, next=answer)

        return answer