class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # think if we should iterate s or t
        # since we want s to be a substring of t, we want to iterate over t
        # if we hit the end of s before t, then we must append the rest of t
        l = 0
        r = 0
        sLen = len(s)
        tLen = len(t)
        while r < tLen:
            # since it is a subsequence, if the current s != r
            # we know the current char can not compose the subsequence
            # increment r if the char is found in s
            # otherwise only increment l
            if s[l] == t[r]:
                l += 1
                r += 1
            else:
                l+= 1
            # if we're done iterating over "s"
            # return remaining num of chars
            if l >= sLen:
                return tLen - r
        
        # if we finish iterating over t, that means the substring is already in s
        return 0