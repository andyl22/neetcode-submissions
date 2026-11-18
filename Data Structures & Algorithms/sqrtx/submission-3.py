class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x

        while l <= r:
            mid = (r + l)//2

            res = mid * mid

            if res == x:
                return mid
            elif res > x:
                r = mid-1
            else:
                l = mid+1
            
        return r


