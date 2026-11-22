class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int[] res = new int[temperatures.length];
        Deque<int[]> tempsAndIndex = new ArrayDeque<>();

        for (int i = 0; i < temperatures.length; i++) {
            res[i] = 0;
            while (tempsAndIndex.size() > 0 && tempsAndIndex.peek()[0] < temperatures[i]) {
                int[] prevTemp = tempsAndIndex.pop();
                res[prevTemp[1]] = i - prevTemp[1];
            }
            tempsAndIndex.push(new int[]{temperatures[i], i});
        }

        return res;
    }
}
