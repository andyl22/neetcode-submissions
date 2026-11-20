class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = len(word1)
        r = len(word2)

        i = 0
        res = []
        while i < l and i < r:
            res.append(word1[i])
            res.append(word2[i])
            i += 1
        
        res.extend(word1[i:])
        res.extend(word2[i:])

        return "".join(res)
        