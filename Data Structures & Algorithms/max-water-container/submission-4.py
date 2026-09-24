class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        maxArea = 0

        while l < r:
            if heights[l] < heights[r]:
                maxArea = max(heights[l] * (r-l), maxArea)
                l += 1
            else:
                maxArea = max(heights[r] * (r-l), maxArea)
                r -= 1
        
        return maxArea