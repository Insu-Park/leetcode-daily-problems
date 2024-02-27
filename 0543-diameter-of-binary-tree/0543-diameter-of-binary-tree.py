# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def getMaxDiameter(node: Optional[TreeNode], res):
            if not node: return 0, res
            left, res = getMaxDiameter(node.left, res)
            right, res = getMaxDiameter(node.right, res)
            res = max(res, left + right)
            return max(left, right) + 1, res

        return getMaxDiameter(root, 0)[1]
        