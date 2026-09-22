class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            bucket = [0]*26
            for c in s:
                bucket[ord(c)-ord("a")] += 1
            res[str(bucket)].append(s)
        return [v for v in res.values()]