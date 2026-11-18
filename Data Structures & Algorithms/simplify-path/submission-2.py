class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")

        for p in path:
            match p:
                case "..":
                    if stack:
                        stack.pop()
                case ".":
                    continue
                case "":
                    continue
                case _:
                    stack.append(p)
        
        return "/" + "/".join(stack)