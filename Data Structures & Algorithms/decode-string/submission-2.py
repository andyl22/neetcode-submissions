class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_string = ""
        current_number = ""

        for i in range(len(s)):
            char = s[i]
            if char == "[":
                stack.append((current_string, current_number))
                current_string = ""
                current_number = ""
            elif char == "]":
                prev = stack.pop()
                current_string = prev[0] + (current_string * int(prev[1]))
            elif char.isdigit():
                current_number += char
            else:
                current_string += char
        
        return current_string
            