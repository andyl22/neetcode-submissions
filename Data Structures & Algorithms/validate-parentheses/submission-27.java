class Solution {
    public boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        Map<Character, Character> lookup = new HashMap<>();
        lookup.put('}', '{');
        lookup.put(']', '[');
        lookup.put(')', '(');

        for (int i = 0; i < s.length(); i++) {
            Character c = s.charAt(i);
            if (lookup.containsKey(c)) {
                if (stack.size() == 0 || lookup.get(c) != stack.pop()) {
                    return false;
                }
            } else {
                stack.push(c);
            }
            
        }

        return stack.size() > 0 ? false : true;
    }
}
