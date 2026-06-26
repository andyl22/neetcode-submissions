class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = Counter(s1)
        s2Count = defaultdict(int)

        slow = 0
        matches = len(s1Count)

        for fast in range(len(s2)):
            s2Char = s2[fast]
            s2Count[s2Char] += 1
            if s1Count[s2Char] == s2Count[s2Char]:
                matches -= 1
            if fast-slow+1 > len(s1):
                if s2Count[s2[slow]] == s1Count[s2[slow]]:
                    matches += 1
                s2Count[s2[slow]] -= 1
                slow += 1

            if matches == 0:
                return True
        
        return False
