class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ast = []

        for c in asteroids:
            while ast and c and c < 0 and ast[-1] > 0:
                if abs(c) > ast[-1]:
                    ast.pop()
                elif abs(c) == ast[-1]:
                    ast.pop()
                    c = None
                else:
                    c = None
            if c:
                ast.append(c)
        
        return ast