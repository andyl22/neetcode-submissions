class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_str = ""
        cur_len = ""

        for i in range(len(s)):
            c = s[i]
            if c == "[":
                stack.append((cur_str,int(cur_len)))
                cur_str = ""
                cur_len = ""
            elif c == "]":
                prev_string, multi = stack.pop()
                cur_str = prev_string + (multi * cur_str)
            elif c.isdigit():
                cur_len += c
            else:
                cur_str += c
        
        return cur_str
