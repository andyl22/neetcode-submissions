class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = [0 for _ in range(26)]
        s2Count = [0 for _ in range(26)]
        for c in s1:
            s1Count[ord(c) - ord('a')] += 1

        i = 0
        j = 0

        while j < len(s2):
            if j - i >= len(s1):
                s2Count[ord(s2[i]) - ord('a')] -= 1
                i += 1
            s2Count[ord(s2[j]) - ord('a')] += 1
            if s1Count == s2Count:
                return True
            j += 1
        
        return False