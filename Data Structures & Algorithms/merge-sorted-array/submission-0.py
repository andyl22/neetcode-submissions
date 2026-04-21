class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # We use a queue to store elements we 'bumped' out of nums1
        buffer = deque()
        
        p1 = 0  # Pointer for nums1 original elements
        p2 = 0  # Pointer for nums2
        
        # We iterate through the entire length of the final nums1
        for i in range(m + n):
            # 1. Get the current value from nums1 (if it exists)
            # If i < m, it's an original element. We move it to the buffer.
            if i < m:
                buffer.append(nums1[i])
            
            # 2. Decide which value to place at nums1[i]
            # We compare the front of our buffer vs the current nums2 element
            
            # Use value from buffer if:
            # - nums2 is empty
            # - OR buffer's front is smaller than nums2's current element
            if p2 >= n or (buffer and buffer[0] <= nums2[p2]):
                nums1[i] = buffer.popleft()
            else:
                # Otherwise, take from nums2
                nums1[i] = nums2[p2]
                p2 += 1