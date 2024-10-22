# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        level_sum = [0] * 100000
        def dfs(node, level):
            nonlocal level_sum
            if node:
                level_sum[level] += node.val
                dfs(node.left, level + 1)
                dfs(node.right, level + 1)
            return

        dfs(root, 0)
        level_sum.sort(reverse=True)
        return level_sum[k - 1] if level_sum[k - 1] != 0 else -1

