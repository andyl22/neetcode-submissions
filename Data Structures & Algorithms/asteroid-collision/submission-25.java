class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Deque<Integer> stack = new ArrayDeque<>();

        outer:
        for (int a: asteroids) {
            boolean alive = true;
            while(stack.size() > 0 && a < 0 && stack.peek() > 0) {
                int abs_a = Math.abs(a);
                int lastAsteroid = Math.abs(stack.peek());
                if(abs_a == lastAsteroid) {
                    stack.pop();
                    continue outer;
                } else if (abs_a > lastAsteroid) {
                    stack.pop();
                } else {
                    continue outer;
                }
            }
            stack.push(a);
        }
        int[] res = new int[stack.size()];
        for (int i = res.length - 1; i >= 0; i--) {
            res[i] = stack.pop();
        }
        return res;
    }
}