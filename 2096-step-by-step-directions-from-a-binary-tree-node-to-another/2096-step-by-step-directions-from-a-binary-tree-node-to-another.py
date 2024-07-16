# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        startPath, endPath = '', ''
        def dfs(node, path):
            if node:
                nonlocal startPath, endPath
                if node.val == startValue:
                    startPath = 'U' * len(path)
                elif node.val == destValue:
                    endPath = path

                dfs(node.left, path + 'L')
                dfs(node.right, path + 'R')

        dfs(root, '')
        return startPath + endPath
