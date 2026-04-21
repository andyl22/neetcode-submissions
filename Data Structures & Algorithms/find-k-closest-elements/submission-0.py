class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # looking for x
        # binary search to find x
        # look to the left. if abs(x-left) <= abs(x-right), take the left pointer

        l, r = 0, len(arr)-1

        while l <= r:
            mid = (r+l) //2
            if arr[mid] == x:
                l = mid-1
                r = mid+1
            if arr[mid] > x:
                r = mid-1
            else:
                l = mid+1
        
        if l > r:
            l, r = r, l
        
        found = []
        while len(found) < k:
            if l < 0:
                found.append(arr[r])
                r += 1
            elif r > len(arr)-1:
                found.append(arr[l])
                l -= 1
            elif abs(x-arr[l]) <= abs(x-arr[r]):
                found.append(arr[l])
                l -= 1
            else:
                found.append(arr[r])
                r += 1
        
        found.sort()
        return found

