# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode]) -> List[int]:
            ret = []
            if not root.left and not root.right:
                return [root.val]
            if root.left:
                ret.extend(dfs(root.left))
            if root.right:
                ret.extend(dfs(root.right))
            return ret
        return dfs(root1) == dfs(root2)