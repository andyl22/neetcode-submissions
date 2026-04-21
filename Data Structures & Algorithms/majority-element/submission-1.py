class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        most = 0
        track = defaultdict(int)

        for n in nums:
            track[n] += 1
            if track[n] > track[most]:
                most = n
        return most