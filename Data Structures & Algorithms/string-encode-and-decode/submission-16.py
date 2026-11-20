class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        l = 0
        r = len(s)-1
        res = []

        while l < r: 
            j = l
            while s[j] != "#":
                j += 1
            length = int(s[l:j])
            j += 1
            res.append(s[j:j+length])
            l = j+length
        
        return res