class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p, s] for p, s in zip(position, speed)]
        pairs.sort(key=lambda x: x[0], reverse=True)
        last = 0
        fleets = 0

        for p in pairs:
            # calculate time to get to target
            cur = float(target - p[0]) / p[1]
            # if time to get to target is less than prev, this car is absorbed into the fleet
            if cur > last:
                last = cur
                fleets += 1

        return fleets