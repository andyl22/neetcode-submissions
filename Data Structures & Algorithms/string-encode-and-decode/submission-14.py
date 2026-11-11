class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        l = 0
        res = []
        while l < len(s):
            j = l
            while s[j] != "#":
                j += 1
            
            length = int(s[l:j])
            
            word = s[j+1:j+length+1]
            res.append(word)
            l = j+length+1
        
        return res