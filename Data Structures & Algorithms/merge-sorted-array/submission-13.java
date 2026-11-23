class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int r = m + n -1;
        m--;
        n--;

        while (n >= 0 && m >= 0) {
            if(nums2[n] >= nums1[m]) {
                nums1[r] = nums2[n];
                n--;
            } else {
                nums1[r] = nums1[m];
                m--;
            }
            r--;
        }

        while (n >= 0){
            nums1[r] = nums2[n];
            n--;
            r--;
        }

        
    }
}