class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Deque<Integer> stack = new ArrayDeque<>();

        for (int a: asteroids) {
            boolean alive = true;
            while(stack.size() > 0 && a < 0 && stack.peek() > 0) {
                int abs_a = Math.abs(a);
                int lastAsteroid = Math.abs(stack.peek());
                if(abs_a == lastAsteroid) {
                    stack.pop();
                    alive = false;
                    break;
                } else if (abs_a > lastAsteroid) {
                    stack.pop();
                    alive = true;
                } else {
                    alive = false;
                    break;
                }
            }
            if (alive) {
                stack.push(a);
            }
        }
        int[] res = new int[stack.size()];
        int i = stack.size()-1;
        for(Integer a: stack) {
            res[i] = a;
            i--;
        }
        return res;
    }
}