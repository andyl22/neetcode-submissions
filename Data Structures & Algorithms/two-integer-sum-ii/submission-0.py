class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1

        while l <= r:
            remainder = target - (numbers[l] + numbers[r])
            if remainder == 0:
                return [l+1,r+1]
            elif remainder>0:
                l+=1
            elif remainder<0:
                r-=1