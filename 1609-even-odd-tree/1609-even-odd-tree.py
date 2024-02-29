# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        tree = [] 
        def visitNode(node, depth, loc):
            if not node: return
            if len(tree) <= depth:
                tree.append({})
                
            tree[depth][loc] = node.val
            visitNode(node.left, depth + 1, loc * 2)
            visitNode(node.right, depth + 1, loc * 2 + 1)
            
        visitNode(root, 0, 0)
        for level, row in enumerate(tree):
            tmp = []
            for key, item in sorted(row.items()):
                if item != 0 and item % 2 == level % 2:
                    return False
                elif item != 0:
                    tmp.append(item)

            if level % 2 == 0 and tmp != sorted(tmp):
                return False
            if level % 2 == 1 and tmp != sorted(tmp, reverse=True):
                return False
            if len(tmp) != len(set(tmp)):
                return False

        return True