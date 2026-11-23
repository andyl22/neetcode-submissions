class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> counter = new HashMap<>();

        for (int n: nums) {
            counter.put(n, counter.getOrDefault(n, 0) +1);
        }
        PriorityQueue<int[]> topK = new PriorityQueue<>((a,b) -> Integer.compare(a[1],b[1]));

        for(Map.Entry<Integer,Integer> entry: counter.entrySet()) {
            Integer n = entry.getKey();
            Integer v = entry.getValue();
            topK.offer(new int[]{n,v});
            if(topK.size()>k) topK.poll();
        }

        int[] res = new int[k];
        int index = 0;
        while(topK.size() > 0) {
            res[index] = topK.poll()[0];
            index++;
        }
        return res;
    }
}
