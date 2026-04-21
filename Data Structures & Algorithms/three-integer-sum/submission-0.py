class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # iterate through the sorted array
        # if the cur number = 0, there is no possible way to sum up to 0 uniquely since the array is sorted
        # for each n, look at the window to the right

        res = []
        visited = set()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            
            if nums[i] in visited:
                continue
            
            visited.add(nums[i])
            
            left = i+1
            right = len(nums) - 1

            while left < right:
                total = nums[left] + nums[right] + nums[i]
                if total == 0:
                    res.append([nums[i],nums[left],nums[right]])
                    # Move left forward past any identical numbers
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Move right backward past any identical numbers
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total>0:
                    right -= 1
                elif total<0:
                    left += 1
        return res
