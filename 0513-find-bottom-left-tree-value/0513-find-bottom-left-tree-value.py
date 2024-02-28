# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.bottom_left_depth = 0
        self.bottom_left_loc = 10 ** 9 + 1
        self.bottom_left_val = 0

        def findBottomLeftVal(node, depth, loc): 
            if not node: return
            if self.bottom_left_depth < depth or (self.bottom_left_depth == depth and self.bottom_left_loc > loc):
                self.bottom_left_depth = depth
                self.bottom_left_loc = loc
                self.bottom_left_val = node.val
            
            findBottomLeftVal(node.left, depth + 1, loc * 2)
            findBottomLeftVal(node.right, depth + 1, loc * 2 + 1)
        
        findBottomLeftVal(root, 0, 0)
        return self.bottom_left_val
