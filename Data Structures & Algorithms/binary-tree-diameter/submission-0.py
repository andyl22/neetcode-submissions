# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        stack = []
        nMap = {None: 0}
        cur = root
        lastVisited = None

        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            # check if we visited the right node yet
            else:
                peek = stack[-1]
                if peek.right and peek.right != lastVisited:
                    cur=peek.right
                else:
                    node = stack.pop()
                    L = nMap[node.left]
                    R = nMap[node.right]
                    diameter = max(diameter, L + R)
                    nMap[node] = 1 + max(L, R)
                    lastVisited = node
                    cur = None
        return diameter