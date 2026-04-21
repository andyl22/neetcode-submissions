class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p, s] for p, s in zip(position, speed)]
        pairs.sort(key=lambda x: x[0], reverse=True)
        stack = []

        for p in pairs:
            # calculate time to get to target
            cur = float(target - p[0]) / p[1]
            if stack:
                peek = stack[-1]
                # if time to get to target is less than prev, this car is absorbed into the fleet
                # don't add it to the stack
                if cur <= peek:
                    continue
                else:
                    stack.append(cur)
            else:
                stack.append(cur)

        return len(stack)