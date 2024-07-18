# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        answer = 0
        def dfs(node, deep):
            nonlocal answer
            # 자식 노드일 때
            if not node:
                return []

            if not node.left and not node.right:
                return [deep]

            left_leafs = dfs(node.left, deep + 1)
            right_leafs = dfs(node.right, deep + 1)

            for left_leaf in left_leafs:
                for right_leaf in right_leafs:
                    if distance >= (left_leaf - deep) + (right_leaf - deep):
                        answer += 1
            
            else:
                return left_leafs + right_leafs

        dfs(root, 0)
        return answer