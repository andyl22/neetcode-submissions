class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            "{": "}",
            "[": "]",
            "(": ")"
        }

        for c in s:
            if c in "{[(":
                stack.append(c)
            else:
                if not stack or mapping[stack.pop()] != c:
                    return False
        return True if not stack else False