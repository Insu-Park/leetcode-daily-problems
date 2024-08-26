"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        answer = []
        def search(node):
            if node:
                for c in node.children:
                    search(c)
                answer.append(node.val)
        
        search(root)
        return answer