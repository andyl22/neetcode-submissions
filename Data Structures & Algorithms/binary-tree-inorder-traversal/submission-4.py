# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        result = []
        # add root to stack then go to the left
        # once root is None, we need to pop the stack and set that as root again
        # if the popped Node has a left, repeat the above
        # we'll get back to the original node eventually when the stack is empty
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            result.append(root.val)

            root = root.right
        return result
