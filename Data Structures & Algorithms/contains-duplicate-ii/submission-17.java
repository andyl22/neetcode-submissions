class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        int slow = 0;
        Set<Integer> seen = new HashSet<>();
        for(int i = 0; i < nums.length; i++) {
            if (i-slow > k) {
                seen.remove(nums[slow]);
                slow++;
            }
            if (seen.contains(nums[i])) {
                return true;
            }
            seen.add(nums[i]);
        }
        return false;


    }
}