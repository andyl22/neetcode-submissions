class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        for c in s:
            if c in "{[(":
                stack.append(c)
            else:
                if not stack:
                    return False
                p = stack.pop()
                if mapping[c] != p:
                    return False
        return True if not stack else False