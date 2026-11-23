class Solution {
    public int lastStoneWeight(int[] stones) {
        // since smashing will reduce the winning stones size, need to continually evict and add
        PriorityQueue<Integer> q = new PriorityQueue<>((a,b) -> Integer.compare(b,a));
        for(int s: stones) {
            q.offer(s);
        }

        while(q.size() > 1) {
            int stone1 = q.poll();
            int stone2 = q.poll();
            q.offer(stone1-stone2);
        }

        return q.poll();
    }
}
