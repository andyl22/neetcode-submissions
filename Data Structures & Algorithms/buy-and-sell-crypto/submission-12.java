class Solution {
    public int maxProfit(int[] prices) {
        int best = 0;
        int min = 1000;

        for (int i = 0; i < prices.length; i++) {
            min = Math.min(min, prices[i]);
            best = Math.max(best,prices[i] - min);
        }

        return best;
    }
}
