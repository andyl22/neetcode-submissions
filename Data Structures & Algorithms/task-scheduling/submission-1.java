class Solution {
    public int leastInterval(char[] tasks, int n) {
        PriorityQueue<Integer> ready = new PriorityQueue<>((a,b) -> Integer.compare(b,a));
        PriorityQueue<int[]> cooldown = new PriorityQueue<>((a,b) -> Integer.compare(a[0],b[0]));
        int cycle = 0;
        int[] freq = new int[26];
        for(int i =0; i< tasks.length; i++) {
            Character c = tasks[i];
            freq[c-'A']++;
        }

        for(int i = 0; i < freq.length; i++) {
            if(freq[i] > 0) ready.offer(freq[i]);
        }

        while (!ready.isEmpty() || !cooldown.isEmpty()) {
            while (cooldown.size() > 0 && cooldown.peek()[0] == cycle) {
                ready.offer(cooldown.poll()[1]);
            };
            if (ready.size() > 0) {
                int remaining = ready.poll()-1;
                if (remaining>0) {
                    cooldown.offer(new int[]{cycle+n+1,remaining});
                }
            }
            cycle++;
        }
        return cycle;
    }
}
