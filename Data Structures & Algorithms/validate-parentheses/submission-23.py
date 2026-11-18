class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        for c in s:
            if c in "}])":
                if not len(stack) or stack.pop() != m[c]:
                    return False
            else:    
                stack.append(c)
        return not len(stack)
