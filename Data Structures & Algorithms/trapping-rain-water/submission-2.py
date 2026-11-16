class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        lMax = height[l]
        rMax = height[r]
        cumulative = 0

        while l < r:
            if rMax > lMax:
                l += 1
                if lMax > height[l]:
                    cumulative += min(rMax, lMax) - height[l]
                else:
                    lMax = height[l]
            else:
                r -= 1
                if rMax > height[r]:
                    cumulative += min(rMax, lMax) - height[r]
                else:
                    rMax = height[r]
        
        return cumulative