class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = ""

        # start a loop which iterates over all chars in first string
        for i, c in enumerate(strs[0]):
            # for each string in strs list
            for s in strs:
                # check if out of bounds
                if i >= len(s):
                    return longest
                # if mismatch, return longest
                if s[i] != c:
                    return longest
            longest += c
        return longest