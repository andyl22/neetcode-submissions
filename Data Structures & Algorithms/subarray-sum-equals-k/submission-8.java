class Solution {
    public int subarraySum(int[] nums, int k) {
        Map<Integer, Integer> prefixes = new HashMap<>();
        prefixes.put(0, 1);
        int counts = 0;
        int rollingSum = 0;

        for (int i = 0; i < nums.length; i++) {
            rollingSum += nums[i];
            int remainder = rollingSum - k;
            if(prefixes.containsKey(remainder)) {
                counts += prefixes.get(remainder);
            }

            prefixes.put(rollingSum,prefixes.getOrDefault(rollingSum, 0)+1);
        }

        return counts;
    }
}