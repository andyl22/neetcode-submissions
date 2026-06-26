class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area = w*h
        # move to the smaller wall, in hopes of finding a taller wall
        # since we are sacrificing area
        l, r = 0, len(heights)-1
        minHeight = 1000
        maxArea = 0

        while l < r:
            minHeight = min(heights[l], heights[r])
            maxArea = max(minHeight*(r-l), maxArea)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return maxArea