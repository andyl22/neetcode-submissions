class Solution {
    private record State(int i, boolean bought) {}
    private Map<State, Integer> memo = new HashMap<>();

    private int rec(int[] prices, int i, boolean bought) {
        if(prices.length==i) {
            return 0;
        }
        int res = 0;
        State memoKey = new State(i, bought);
        if (memo.containsKey(memoKey)) {
            return memo.get(memoKey);
        }

        res = rec(prices, i+1, bought);

        if (bought == true) {
            res = Math.max(res, prices[i] + rec(prices, i+1, false));
        } else {
            res = Math.max(res, -prices[i] + rec(prices, i+1, true));
        }

        memo.put(memoKey, res);
        return res;
    }

    public int maxProfit(int[] prices) {
        return rec(prices, 0, false);
    }
}