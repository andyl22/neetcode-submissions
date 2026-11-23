class Solution {
    public int maxProfit(int[] prices) {
        int best = 0;
        int minPrice = 1000;

        for(int i =0; i < prices.length; i++) {
            minPrice = Math.min(minPrice, prices[i]);
            best = Math.max(best, prices[i] - minPrice);
        }

        return best;
    }
}
