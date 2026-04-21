class Solution:
    def simplifyPath(self, path: str) -> str:
        split = path.split("/")
        stack = []

        for s in split:
            if s == "" or s == ".":
                continue
            elif s == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(s)
        
        return "/" + "/".join(stack)