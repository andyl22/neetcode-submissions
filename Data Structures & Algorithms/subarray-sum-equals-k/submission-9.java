class Solution {
    public int subarraySum(int[] nums, int k) {
        // [10,2,3,6]
        // [10, 12, 15, 21]
        // 15 - 5 (k). we need a subarray start from 10. index 1.
        // use a hashmap to keep track of hte number of occurence of 10 to get the total number of subarrays that sum to k
        int rollingSum = 0;
        int count = 0;
        Map<Integer, Integer> prefixCounts = new HashMap<>();
        prefixCounts.put(0, 1);

        for(int i = 0; i < nums.length; i++) {
            rollingSum += nums[i];
            int subArrayStartValue = rollingSum - k;
            if(prefixCounts.containsKey(subArrayStartValue)) {
                count += prefixCounts.get(subArrayStartValue);
            }
            prefixCounts.merge(rollingSum, 1, Integer::sum);
        }

        return count;
    }
}