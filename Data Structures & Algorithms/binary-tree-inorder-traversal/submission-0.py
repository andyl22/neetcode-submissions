# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.recurse(root, res)
        return res
    
    def recurse(self, node, res):
        if not node:
            return
        
        # 1. Traverse the left subtree
        self.recurse(node.left, res)
        
        # 2. Visit the current node
        res.append(node.val)
        
        # 3. Traverse the right subtree
        self.recurse(node.right, res)