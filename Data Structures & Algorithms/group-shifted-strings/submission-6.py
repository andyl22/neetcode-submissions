class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        res = []
        diffs = defaultdict(list)

        for i in range(len(strings)):
            key = tuple((ord(strings[i][c+1]) - ord(strings[i][c])) % 26 for c in range(len(strings[i])-1))
            diffs[key].append(strings[i])

        for group in diffs.values():
            res.append(group)
        return res