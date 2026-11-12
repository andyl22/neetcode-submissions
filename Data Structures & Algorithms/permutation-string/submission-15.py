class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Bucket = [0 for _ in range(26)]
        for c in s1:
            s1Bucket[ord(c) - ord('a')] += 1
        
        l, r = 0, 0

        s2Bucket = [0 for _ in range(26)]
        while r < len(s2):
            s2Bucket[ord(s2[r]) - ord('a')] += 1
            if r - l == len(s1):
                s2Bucket[ord(s2[l]) - ord('a')] -= 1
                l += 1
            if s2Bucket == s1Bucket:
                return True
            r += 1
        
        return False