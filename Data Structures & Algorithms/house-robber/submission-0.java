class Solution {
    private Map<Integer, Integer> memo = new HashMap<>();

    public int rob(int[] nums) {
        return robHouse(0, nums);
    }

    private int robHouse(int i, int[] nums) {
        if (i >= nums.length) {
            return 0;
        }

        if(memo.containsKey(i)) return memo.get(i);

        int res = Math.max(robHouse(i+1,nums), robHouse(i+2,nums) + nums[i]);
        memo.put(i, res);
        return res;
    }
}
