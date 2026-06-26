class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # slow pointer
        # move the slow pointer up until 
        # we remove the s[fast] from the character set
        cSet = set()
        slow = 0
        best = 0
        for r in range(len(s)):
            while s[r] in cSet:
                cSet.remove(s[slow])
                slow += 1
            cSet.add(s[r])
            best = max(best, r - slow + 1)
        
        return best
