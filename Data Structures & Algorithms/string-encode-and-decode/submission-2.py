class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded = []

        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length=int(s[i:j])

            j += 1
            k = j
            while length:
                k += 1
                length -= 1
            decoded.append(s[j:k])
            i = k
        
        return decoded






            

