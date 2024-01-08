# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.find_val(root, low, high)

    def find_val(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0 
        current = 0
        if low <= root.val <= high:
            current = root.val
        left = self.find_val(root.left, low, high) 
        right = self.find_val(root.right, low, high)
        return current + left + right