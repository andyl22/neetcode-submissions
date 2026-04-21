# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        stack = []
        cur = root
        hMap = {None: 0}
        last_visited = None

        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                peek = stack[-1].right
                if peek and peek != last_visited:
                    stack.append(peek)
                    cur = peek
                else:
                    n = stack.pop()
                    last_visited = n
                    l = hMap[n.left]
                    r = hMap[n.right]
                    if abs(l - r) > 1:
                        return False
                    hMap[n] = 1 + max(l, r)
                    cur = None
        
        return True
