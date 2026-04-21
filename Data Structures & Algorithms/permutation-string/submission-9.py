class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        c2 = defaultdict(int)

        i = 0
        matches = 0
        expected = len(c1)
        wSize = len(s1)

        for j, char in enumerate(s2):
            c2[char] += 1

            if char in c1:
                if c2[char] == c1[char]:
                    matches += 1

            if j - i + 1 > wSize:
                delC = s2[i]
                if c1[delC] == c2[delC]:
                    matches -= 1
                c2[delC] -= 1
                i+=1
            
            if matches == expected:
                return True
        
        return False

