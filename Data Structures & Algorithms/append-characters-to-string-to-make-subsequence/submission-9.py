class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        tPtr = 0
        tLen = len(t)
        for c in s:
            if tPtr >= tLen:
                return 0
            if c == t[tPtr]:
                tPtr += 1
        
        return tLen - tPtr
