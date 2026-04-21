class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ast = []

        for cur in asteroids:
            if len(ast):
                while ast and cur and (cur < 0 and ast[-1] > 0):
                    if abs(cur) == ast[-1]:
                        cur = None
                        ast.pop()
                        break
                    elif abs(cur) < ast[-1]:
                        cur = None
                    else:
                        ast.pop()

            if cur:
                ast.append(cur)
        
        return ast