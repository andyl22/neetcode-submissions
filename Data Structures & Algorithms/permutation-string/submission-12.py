class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Counted = [0 for _ in range(26)]
        for i in s1:
            s1Counted[ord(i) - ord('a')] += 1
        s2Counted = [0 for _ in range(26)]
        slow = 0
        fast = 0
        
        while fast < len(s2):
            if fast-slow+1 > len(s1):
                s2Counted[ord(s2[slow]) - ord('a')] -= 1
                slow += 1
            s2Counted[ord(s2[fast]) - ord('a')] += 1
            if s2Counted == s1Counted:
                return True
            fast += 1
        
        return False