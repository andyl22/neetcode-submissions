class Solution {
    public String decodeString(String s) {
        record Frame(String prev, Integer multiplier) {};

        Deque<Frame> prevInfo = new ArrayDeque<>();
        StringBuilder curString = new StringBuilder();
        StringBuilder curLength = new StringBuilder();

        for (int i =0; i < s.length(); i++) {
            Character c = s.charAt(i);
            if(c == '[') {
                prevInfo.push(new Frame(curString.toString(), Integer.parseInt(curLength.toString())));
                curString.setLength(0);
                curLength.setLength(0);
            } else if (c == ']') {
                Frame last = prevInfo.pop();
                StringBuilder tempString = new StringBuilder(last.prev());
                for (int j = 0; j < last.multiplier(); j++) {
                    tempString.append(curString);
                }
                curString = tempString;
            } else if (Character.isDigit(c)) {
                curLength.append(c);
            } else {
                curString.append(c);
            }
        }

        return curString.toString();
    }
}