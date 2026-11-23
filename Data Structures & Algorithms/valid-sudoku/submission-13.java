class Solution {
    public boolean isValidSudoku(char[][] board) {
        List<Set<Character>> row = new ArrayList<>();
        List<Set<Character>> col = new ArrayList<>();
        List<List<Set<Character>>> boards = new ArrayList<>();

        for(int i = 0; i<9; i++) {
            List<Set<Character>> sets = new ArrayList<>();
            for(int j = 0; j<9; j++) {
                sets.add(new HashSet<>());
            }
            boards.add(sets);
            row.add(new HashSet<>());
            col.add(new HashSet<>());
        }

        for(int i = 0; i<9; i++) {
            for(int j = 0; j<9; j++) {
                char cell = board[i][j];
                if(cell == '.') continue;
                if(row.get(i).contains(cell) || col.get(j).contains(cell) || boards.get(i/3).get(j/3).contains(cell)) return false;
                row.get(i).add(cell);
                col.get(j).add(cell);
                boards.get(i/3).get(j/3).add(cell);
            }
        }

        return true;
    }
}
