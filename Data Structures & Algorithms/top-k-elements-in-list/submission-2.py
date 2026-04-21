class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] += 1
        
        for key, value in count.items():
            freq[value].append(key)

        result = []
        for i in range(len(freq) - 1, 0, -1):
            for value in freq[i]:
                result.append(value)
                if len(result) == k:
                    return result