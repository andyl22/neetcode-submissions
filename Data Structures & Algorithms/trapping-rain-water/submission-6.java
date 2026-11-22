class Solution {
    public int trap(int[] height) {
        int l = 0;
        int r = height.length-1;
        int lMax = height[0];
        int rMax = height[r];
        int total = 0;

        while (l < r) {
            if(lMax > rMax) {
                r--;
                rMax = Math.max(rMax, height[r]);
                total += rMax - height[r];
            } else {
                l++;
                lMax = Math.max(lMax,height[l]);
                total += lMax - height[l];
            }
        }
        return total;
    }
}
