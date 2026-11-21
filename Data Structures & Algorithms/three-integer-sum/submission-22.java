class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        int i = 0;
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();

        while (i < nums.length) {
            if (i > 0 && nums[i] == nums[i-1]) {
                i += 1;
                continue;
            }
            int j = i + 1;
            int k = nums.length - 1;
            while (j < k) {
                int total = nums[i] + nums[j] + nums[k];
                if (total == 0) {
                    List<Integer> sums = new ArrayList<>();
                    sums.add(nums[i]);
                    sums.add(nums[j]);
                    sums.add(nums[k]);
                    res.add(sums);
                    k--;
                    j++;
                    while (j < k && nums[k] == nums[k+1]) {
                        k--;
                    }
                    while (j < k && nums[j] == nums[j-1]) {
                        j++;
                    }
                } else if (total > 0) {
                    k--;
                } else {
                    j++;
                }
            }
            i += 1;
        }

        return res;
    }
}
