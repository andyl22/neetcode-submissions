# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        lastVisited = None

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            else:
                peek = stack[-1]
                if peek.right and lastVisited != peek.right:
                    root = peek.right
                else:
                    root = stack.pop()
                    res.append(root.val)
                    lastVisited = root
                    root = None
        return res