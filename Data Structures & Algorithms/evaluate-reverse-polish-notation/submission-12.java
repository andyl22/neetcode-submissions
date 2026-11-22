class Solution {
    public int evalRPN(String[] tokens) {
        Deque<Integer> stack = new ArrayDeque<>();

        for (String t: tokens) {
            switch(t) {
                case "+" -> {
                    int[] values = getLastTwoValues(stack);
                    stack.push(values[1] + values[0]);
                }
                case "-" -> {
                    int[] values = getLastTwoValues(stack);
                    stack.push(values[1] - values[0]);
                }
                case "*" -> {
                    int[] values = getLastTwoValues(stack);
                    stack.push(values[1] * values[0]);
                }
                case "/" -> {
                    int[] values = getLastTwoValues(stack);
                    stack.push(values[1] / values[0]);
                }
                default -> stack.push(Integer.parseInt(t));
            }
        }
        return stack.pop();
    }

    private int[] getLastTwoValues(Deque<Integer> stack) {
        return new int[]{stack.pop(), stack.pop()};
    }
}
