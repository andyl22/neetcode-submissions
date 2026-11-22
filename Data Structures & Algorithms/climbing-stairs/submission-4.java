class Solution {
    private HashMap<Integer, Integer> memo = new HashMap<>();
    public int climbStairs(int n) {
        return climb(n, 0);
    }

    private int climb(int target, int cur) {
        if (cur > target) return 0;
        if (cur == target) return 1;

        if(memo.containsKey(cur)) return memo.get(cur);
        int res = climb(target, cur+1) + climb(target, cur+2);
        memo.put(cur, res);
        return res;
    }
}
