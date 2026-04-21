# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        stack = [(root,1)]
        best = 0

        while stack:
            cur = stack.pop()
            n, v = cur
            best = max(best, v)
            if n.right:
                stack.append((n.right, v+1))
            if n.left:
                stack.append((n.left, v+1))

        return best