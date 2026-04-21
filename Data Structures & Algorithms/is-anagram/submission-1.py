class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)): 
          return False
        chars = {}
        for i in range(len(s)):
            sChar = s[i]
            tChar = t[i]
            chars[sChar] = chars.get(sChar, 0) + 1
            chars[tChar] = chars.get(tChar, 0) - 1
        return all(value == 0 for value in chars.values())
          