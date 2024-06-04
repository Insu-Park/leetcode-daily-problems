# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def traverse(node: TreeNode) -> int:
            if not node:
                return 0
            left_excess = traverse(node.left)
            right_excess = traverse(node.right)
            total_excess = node.val + left_excess + right_excess - 1
            self.moves += abs(total_excess)
            return total_excess

        self.moves = 0
        traverse(root)
        return self.moves