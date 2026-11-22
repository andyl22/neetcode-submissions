class Solution {
    public int removeDuplicates(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        int slow = 0;
        for(int i = 0; i < nums.length; i++) {
            if (!seen.contains(nums[i])) {
                nums[slow] = nums[i];
                slow++;
                seen.add(nums[i]);
            }
        }

        return slow;
    }
}