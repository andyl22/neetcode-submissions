class Solution {
    public int removeDuplicates(int[] nums) {
        Set<Integer> seen = new HashSet<>();

        int k = 0;
        for (int n: nums) {
            if(!seen.contains(n)) {
                nums[k] = n;
                k++;
            } 
            seen.add(n);
            
            
        }

        return k;
    }
}