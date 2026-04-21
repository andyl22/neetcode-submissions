class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map1=defaultdict(int)
        map2=defaultdict(int)
        matches = 0

        for s in s1:
            map1[s] += 1

        perfectMatches = len(map1)

        l = 0
        for r in range(len(s2)):
            map2[s2[r]] += 1
            if map2[s2[r]] == map1[s2[r]]:
                matches += 1

            while r - l +1 > len(s1):
                if map2[s2[l]] == map1[s2[l]]:
                    matches -= 1
                map2[s2[l]] -= 1
                l += 1
            if matches == perfectMatches:
                return True
        
        return False