class Solution {
    public String decodeString(String s) {
        record PrevStringData(String prevString, Integer count) {};

        Deque<PrevStringData> prevStringInfo = new ArrayDeque<>();
        StringBuilder curLength = new StringBuilder();
        StringBuilder curString = new StringBuilder();

        for (int i =0; i < s.length(); i++) {
            Character c = s.charAt(i);
            if(c == '[') {
                prevStringInfo.push(new PrevStringData(curString.toString(), Integer.parseInt(curLength.toString())));
                curString = new StringBuilder();
                curLength = new StringBuilder();
            } else if (c== ']') {
                PrevStringData prevStringData = prevStringInfo.pop();
                String prevString = prevStringData.prevString();
                int count = prevStringData.count();
                StringBuilder newString = new StringBuilder();
                newString.append(prevString);
                for (int j = 0; j < count; j++) {
                    newString.append(curString);
                }
                curString = newString;
            } else if (Character.isDigit(c)) {
                curLength.append(c);
            } else {
                curString.append(c);
            }
        }

        return curString.toString();
    }
}