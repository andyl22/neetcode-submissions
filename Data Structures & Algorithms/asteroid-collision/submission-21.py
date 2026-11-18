class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []

        for a in asteroids:
            add = True
            while len(s) and (a < 0 and s[-1] > 0):
                if abs(s[-1]) == abs(a):
                    s.pop()
                    add = False
                    break
                elif abs(s[-1]) > abs(a):
                    add = False
                    break
                else:
                    s.pop()
            if add:
                s.append(a)
        
        return s
