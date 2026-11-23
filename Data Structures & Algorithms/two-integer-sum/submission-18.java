class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> remainder = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int r = target - nums[i];
            if(remainder.containsKey(r)) {
                return new int[]{remainder.get(r), i};
            }
            remainder.put(nums[i], i);
        }

        return new int[]{};
    }
}
