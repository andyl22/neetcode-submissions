class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []

        l = 0
        while l < len(word1) and l < len(word2):
            res.extend([word1[l], word2[l]])
            l+= 1
        
        return "".join(res) + word1[l:] + word2[l:]