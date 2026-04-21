class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = defaultdict(int)
        freq2 = defaultdict(int)

        for s in s1:
            freq1[s] += 1
        
        matches = 0
        perfectMatches = len(freq1)
        
        left = 0
        for right in range(len(s2)):
            curChar = s2[right]
            freq2[curChar] += 1
            if freq2[curChar] == freq1[curChar]:
                matches += 1
            
            while right - left + 1 > len(s1):
                delChar = s2[left]
                if freq2[delChar] == freq1[delChar]:
                    matches -= 1
                freq2[delChar] -= 1
                left += 1
            
            if perfectMatches == matches:
                return True
        
        return False
                