class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = [[] for _ in range(len(nums)+1)]
        c = defaultdict(int)

        for n in nums:
            c[n] += 1

        for key,v in c.items():
            freq[v].append(key)

        for i in range(len(freq)-1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res