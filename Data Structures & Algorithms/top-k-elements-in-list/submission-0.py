class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for key, value in count.items():
            freq[value].append(key)

        result = []
        while k>0:
            values = freq.pop()
            for value in values:
                if k>0:
                    result.append(value)
                    k -= 1
        return result