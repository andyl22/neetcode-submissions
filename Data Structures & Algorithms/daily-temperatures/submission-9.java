class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int[] res = new int[temperatures.length];
        Deque<List<Integer>> tempsAndIndex = new ArrayDeque<>();

        for (int i = 0; i < temperatures.length; i++) {
            res[i] = 0;
            while (tempsAndIndex.size() > 0 && tempsAndIndex.peek().get(0) < temperatures[i]) {
                List<Integer> prevTemp = tempsAndIndex.pop();
                res[prevTemp.get(1)] = i - prevTemp.get(1);
            }
            tempsAndIndex.push(Arrays.asList(temperatures[i], i));
        }

        return res;
    }
}
