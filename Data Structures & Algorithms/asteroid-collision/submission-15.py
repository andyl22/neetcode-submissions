class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ast = []

        for c in asteroids:
            while ast and c < 0 and ast[-1] > 0:
                if abs(c) > ast[-1]:
                    ast.pop()
                    continue
                elif abs(c) == ast[-1]:
                    ast.pop()
                break
            else:
                ast.append(c)
        
        return ast