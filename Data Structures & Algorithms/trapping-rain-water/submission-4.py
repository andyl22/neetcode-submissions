class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
            
        l = 0
        r = len(height)-1
        lMax = height[l]
        rMax = height[r]
        cumulative = 0

        while l < r:
            if rMax > lMax:
                l += 1
                lMax = max(lMax, height[l])
                cumulative += lMax - height[l]
            else:
                r -= 1
                rMax = max(rMax, height[r])
                cumulative += rMax - height[r]
        return cumulative