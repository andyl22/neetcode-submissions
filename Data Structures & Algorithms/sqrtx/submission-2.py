class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        ans = 0

        while l <= r:
            mid = (r + l)//2

            if mid*mid == x:
                return mid
            elif mid*mid < x:
                l = mid + 1
                ans = max(ans, mid)
            else:
                r = mid - 1
            
        return ans
