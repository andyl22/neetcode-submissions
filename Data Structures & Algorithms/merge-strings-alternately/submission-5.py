class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0
        final = ""
        while l < len(word1) and l < len(word2):
            final += word1[l] + word2[l]
            l += 1
        
        return final + word1[l:] + word2[l:]
