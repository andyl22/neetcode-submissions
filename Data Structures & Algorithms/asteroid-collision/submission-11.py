class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i in range(len(asteroids)):
            # we only want to append after we've destroyed colliding asteroids
            # AND we never suicide explode
            cur = asteroids[i]

            if cur < 0:
                while stack and cur:
                    if stack[-1] < 0:
                        break
                    if stack[-1] == abs(cur):
                        stack.pop()
                        cur = None
                        break
                    elif stack[-1] > abs(cur):
                        cur = None
                        break
                    else:
                        stack.pop()
            if cur:
                stack.append(cur)
                    

        return stack
            