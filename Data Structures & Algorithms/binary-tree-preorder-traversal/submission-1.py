# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        stack = [root] # Seeded stack!
        res = []

        while stack: # No 'or cur' needed here!
            node = stack.pop()
            res.append(node.val)
            
            # Push Right then Left so Left is processed first (LIFO)
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
            
        return res