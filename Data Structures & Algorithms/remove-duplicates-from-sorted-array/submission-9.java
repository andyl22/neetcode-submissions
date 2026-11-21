class Solution {
    public int removeDuplicates(int[] nums) {
        int slow = 0;
        Set<Integer> seen = new HashSet<>();

        for(int i = 0; i < nums.length; i++) {
            if(seen.contains(nums[i])) {
                continue;
            }

            seen.add(nums[i]);
            nums[slow] = nums[i];
                slow += 1;
        }

        return slow;
    }
}