class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        count = 0
        start = 0
        
        while count < n:
            curr_idx = start
            curr_val = nums[start]
            
            while True:
                next_idx = (curr_idx + k) % n
                # Swap values
                nums[next_idx], curr_val = curr_val, nums[next_idx]
                
                curr_idx = next_idx
                count += 1
                
                # Close the current cycle when we loop back to start
                if curr_idx == start:
                    break
                    
            # Move to the next independent cycle if needed
            start += 1