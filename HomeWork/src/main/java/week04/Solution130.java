package week04;

public class Solution130 {
    private int m, n;
    private char[][] board;
    private int[] dx = { 1, 0, 0, -1 };
    private int[] dy = { 0, 1, -1, 0 };

    public void solve(char[][] board) {
        this.board = board;
        m = board.length;
        n = board[0].length;

        for (int i = 0; i < m; i++) {
            dfs(i, 0);
            dfs(i, n - 1);
        }

        for (int i = 0; i < n; i++) {
            dfs(0, i);
            dfs(m - 1, i);
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(board[i][j] + " ");
                if (board[i][j] == 'A') {
                    board[i][j] = 'O';
                } else if (board[i][j] == 'O') {
                    board[i][j] = 'X';
                }
            }
            System.out.println();
        }
    }

    private void dfs(int i, int j) {
        if (i < 0 || j < 0 || i >= m || j >= n || board[i][j] != 'O') {
            return;
        }

        board[i][j] = 'A';

        for (int to = 0; to < 4; to++) {
            int ni = i + dx[to];
            int nj = j + dy[to];

            dfs(ni, nj);

        }

    }

    public static void main(String[] args) {
        Solution130 s = new Solution130();

        // char[][] board = {
        // { 'X', 'O', 'X', 'X' },
        // { 'X', 'O', 'O', 'X' },
        // { 'X', 'O', 'O', 'X' },
        // { 'X', 'O', 'X', 'X' },
        // };

        // char[][] board = {
        // { 'X', 'X', 'X', 'X' },
        // { 'X', 'O', 'O', 'X' },
        // { 'X', 'X', 'O', 'X' },
        // { 'X', 'O', 'X', 'X' }
        // };

        char[][] board = {
                { 'X', 'O', 'X', 'O', 'X', 'O' },
                { 'O', 'X', 'O', 'X', 'O', 'X' },
                { 'X', 'O', 'X', 'O', 'X', 'O' },
                { 'O', 'X', 'O', 'X', 'O', 'X' }
        };
        s.solve(board);

    }
}
