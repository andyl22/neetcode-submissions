class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        slow = 0
        fast = 0
        for n in nums:
            if n not in seen:
                seen.add(n)
                nums[slow] = n
                slow += 1
            fast += 1
        return slow
                