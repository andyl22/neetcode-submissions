class Solution {
    public int majorityElement(int[] nums) {
        int cand = 0;
        int freq = 0;

        for(int i = 0; i < nums.length; i++) {
            if(nums[i] == cand) {
                freq++;
            } else {
                freq--;
            }
            if(freq<=0) {
                cand = nums[i];
                freq = 1;
            }
        }

        return cand;
    }
}