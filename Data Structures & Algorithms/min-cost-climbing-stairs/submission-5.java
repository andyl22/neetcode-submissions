class Solution {
    private Map<Integer, Integer> memo = new HashMap<>();
    public int minCostClimbingStairs(int[] cost) {
        return Math.min(climb(cost, 0), climb(cost,1));
    }

    private int climb(int[] cost, int cur) {
        if (cur >= cost.length) {
            return 0;
        }

        if(memo.containsKey(cur)) {
            return memo.get(cur);
        }

        int res = cost[cur] + Math.min(climb(cost, cur+1), climb(cost, cur+2));
        memo.put(cur, res);
        return res;
    }
}
