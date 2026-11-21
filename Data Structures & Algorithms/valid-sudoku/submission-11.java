class Solution {
    public boolean isValidSudoku(char[][] board) {
        List<Set<String>> rows = new ArrayList<>();
        List<Set<String>> cols = new ArrayList<>();
        List<List<Set<String>>> boards = new ArrayList<>();

        for (int r = 0; r < 3; r++) {
            List<Set<String>> set = new ArrayList<>();
            for (int c =0; c <3; c++) {
                rows.add(new HashSet<>());
                cols.add(new HashSet<>());
                set.add(new HashSet<>());
            }
            boards.add(set);
        }

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] == '.') {
                    continue;
                }
                String cell = String.valueOf(board[r][c]);

                if (rows.get(r).contains(cell) || cols.get(c).contains(cell) || boards.get(r/3).get(c/3).contains(cell)) {
                    return false;
                }

                rows.get(r).add(cell);
                cols.get(c).add(cell);
                boards.get(r/3).get(c/3).add(cell);
            }
        }

        return true;
    }
}
