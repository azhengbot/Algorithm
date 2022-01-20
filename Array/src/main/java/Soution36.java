class Solution36 {
    public boolean isValidSudoku(char[][] board) {

        int[][] row = new int[9][9];
        int[][] col = new int[9][9];
        int[][] subBorad = new int[9][9];

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == '.') {

                    continue;
                }

                int num = board[i][j] - '0' - 1;

                int subI = i / 3;
                int subJ = j / 3;
                int subIdx = subI * 3 + subJ;

                if (row[i][num] == 1 || col[j][num] == 1 || subBorad[subIdx][num] == 1) {
                    return false;
                }

                row[i][num] = 1;
                col[j][num] = 1;
                subBorad[subIdx][num] = 1;

            }

        }
        return true;
    }

}