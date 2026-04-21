class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sLen = len(s)
        counter = 0
        for i in range(sLen-1, -1, -1):
            if s[i] != " ":
                counter += 1
            elif counter !=0:
                return counter
        return 1