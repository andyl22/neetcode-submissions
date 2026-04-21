class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 1. Pair and Sort (Descending)
        cars = sorted(zip(position, speed), reverse=True)
        stack = []

        for p, s in cars:
            # 2. Calculate time
            time = (target - p) / s
            
            # 3. Traditional Stack Logic
            # If the stack is empty, or if this car takes LONGER than 
            # the fleet in front, it becomes the lead of a NEW fleet.
            if not stack or time > stack[-1]:
                stack.append(time)
            
            # If time <= stack[-1], we do nothing (the car merges).
            # The stack top remains the bottleneck for everyone further back.
            
        return len(stack)