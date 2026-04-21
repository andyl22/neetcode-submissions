class Solution:
    def decodeString(self, s: str) -> str:
        current_string = ""
        current_number = ""
        prev_string = ""
        stack = []

        for i in range(len(s)):
            c = s[i]
            if c in "0123456789":
                current_number += c
            elif c == "[":
                stack.append((current_number, current_string))
                current_string = ""
                current_number = ""
            elif c == "]":
                if len(stack):
                    p = stack.pop()
                    current_string = p[1] + (int(p[0]) * current_string)
                else:
                    current_string = int(current_number) * current_string
            else:
                current_string += c
        return current_string