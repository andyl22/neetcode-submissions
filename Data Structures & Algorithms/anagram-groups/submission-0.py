class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for x in strs:
            sortedString = ''.join(sorted(x))
            anagrams[sortedString].append(x)
        return anagrams.values()
