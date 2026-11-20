class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse = True)
        fleets = []

        for i,v in enumerate(cars):
            pos, speed = v
            time = (target - pos) / speed
            if fleets and fleets[-1] >= time:
                continue
            else:
                fleets.append(time)
            
        return len(fleets)