class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> numSet = new HashSet<>();
        
        for (int n: nums) {
            numSet.add(n);
        }

        int count = 1;
        int best = 0;
        for (int n: numSet) {
            if (numSet.contains(n-1)) { 
                continue; 
            }
            while (numSet.contains(n+1)) {
                n += 1;
                count += 1;
            }
            best = Math.max(best, count);
            count = 1;
        }

        return best;
    }
}
