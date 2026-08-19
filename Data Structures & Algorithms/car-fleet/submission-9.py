class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = sorted(zip(position, speed), reverse=True)
        last = 0
        fleets = 0

        for p,s in pair:
            time = (target-p)/s
            if time > last:
                fleets += 1
                last = time
            
        return fleets