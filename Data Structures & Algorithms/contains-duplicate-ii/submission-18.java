class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Set<Integer> seen = new HashSet<>();

        int j = 0;
        for (int i = 0; i< nums.length; i++) {
            if(i-j>k) {
                seen.remove(nums[j]);
                j++;
            }
            if(seen.contains(nums[i])) {
                return true;
            }
            seen.add(nums[i]);
        }

        return false;
    }
}