# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        l = []
        def search(node):
            if node:
                nonlocal l
                search(node.left)
                l.append(node)
                search(node.right)

        def makeBalanceBST(start, end):
            if start <= end:
                nonlocal l
                mid = (start + end) // 2
                root = l[mid]
                root.left = makeBalanceBST(start, mid - 1)
                root.right = makeBalanceBST(mid + 1, end)
                return root
        
        search(root)
        return makeBalanceBST(0, len(l) - 1)
