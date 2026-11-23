class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Set<Integer> seen = new HashSet<>();
        int slow = 0;

        for(int fast = 0; fast < nums.length; fast++) {
            if(fast - slow > k) {
                seen.remove(nums[slow]);
                slow++;
            }
            if(seen.contains(nums[fast])) return true;
            seen.add(nums[fast]);
        }
        return false;
    }
}