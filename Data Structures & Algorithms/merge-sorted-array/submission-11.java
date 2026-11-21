class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int r = m + n -1;
        n -= 1;
        m -= 1;

        while (n >= 0 && m >= 0) {
            if (nums1[m] > nums2[n]) {
                nums1[r] = nums1[m];
                m -= 1;
            } else {
                nums1[r] = nums2[n];
                n -= 1;
            }
            r -= 1;
        }

        while (n >= 0) {
            nums1[r] = nums2[n];
            r -= 1;
            n -= 1;
        }

    }
}