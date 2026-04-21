class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ast = []

        for cur in asteroids:
            if len(ast):
                last = ast[-1]
                while (cur and last) and (cur < 0 and last > 0):
                    if abs(cur) == last:
                        cur = None
                        ast.pop()
                        break
                    elif abs(cur) < last:
                        cur = None
                    else:
                        ast.pop()
                        if len(ast):
                            last = ast[-1]
                        else:
                            last = None

            if cur:
                ast.append(cur)
        
        return ast