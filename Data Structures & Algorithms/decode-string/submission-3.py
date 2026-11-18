class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_str = ""
        curr_num = ""
        l = 0

        while l < len(s):
            if s[l].isdigit():
                curr_num += s[l]
            elif s[l] == "[":
                stack.append((int(curr_num), curr_str))
                curr_str = ""
                curr_num = ""
            elif s[l] == "]":
                prev = stack.pop()
                curr_str = prev[1] + (prev[0] * curr_str)

            else:
                curr_str += s[l]
            l += 1
        return curr_str

