# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        cur = root
        stack = []
        res = []
        lastVisited = None

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            else:
                peek = stack[-1]
                if peek.right and peek.right != lastVisited:
                    cur = peek.right
                else:
                    cur = stack.pop()
                    res.append(cur.val)
                    lastVisited = cur
                    cur = None
        return res