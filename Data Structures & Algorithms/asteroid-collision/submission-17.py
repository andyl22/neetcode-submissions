class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ast = []

        for c in asteroids:
            alive = True
            while ast and alive and c < 0 and ast[-1] > 0:
                if abs(c) > ast[-1]:
                    ast.pop()
                elif abs(c) == ast[-1]:
                    ast.pop()
                    alive = False
                else:
                    alive = False
            if alive:
                ast.append(c)
        
        return ast