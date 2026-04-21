class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)-1
        len2 = len(word2)-1

        newWord = ""
        i = 0
        while (i <= min(len1, len2)):
            newWord += word1[i] + word2[i]
            i += 1
            
        return newWord + word1[i::] + word2[i::]