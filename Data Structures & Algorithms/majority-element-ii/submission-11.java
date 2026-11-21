class Solution {
    public List<Integer> majorityElement(int[] nums) {
        int cand1 = 0, cand2 = 0, count1= 0, count2 = 0;

        for (int n: nums) {
            if (n == cand1) {
                count1 += 1;
            } else if (n == cand2) {
                count2 += 1;
            } else if(count1==0) {
                cand1 = n;
                count1 = 1;
            } else if (count2==0) {
                cand2 = n;
                count2 = 1;
            } else {
                count1 -=1;
                count2 -=1;
            }
        }

        int actual1 = 0, actual2 = 0;
        for (int n : nums) {
            if (n == cand1) {
                actual1++;
            } else if (n == cand2) {
                actual2++;
            }
        }


        List<Integer> res = new ArrayList<>();
        int threshold = nums.length / 3;
        if (actual1 > threshold) {
            res.add(cand1);
        }

        if (actual2 > threshold) {
            res.add(cand2);
        }

        return res;
        
    }
}