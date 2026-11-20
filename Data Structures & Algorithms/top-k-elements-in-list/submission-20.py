class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums)+1)]
        counts = Counter(nums)

        for num, freq in counts.items():
            bucket[freq].append(num)
        
        res = []
        bucket.reverse()
        for innerBucket in bucket:
            for value in innerBucket:
                res.append(value)
                if len(res) == k:
                    return res
        
        
