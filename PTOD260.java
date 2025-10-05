import java.util.ArrayList;

class Solution {
    private final int[] dx = {2, 1, -1, -2, -2, -1, 1, 2};
    private final int[] dy = {1, 2, 2, 1, -1, -2, -2, -1};
    private ArrayList<ArrayList<Integer>> board;
    private int n;
    public ArrayList<ArrayList<Integer>> knightTour(int n) {
        this.n = n;
        board = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            ArrayList<Integer> row = new ArrayList<>();
            for (int j = 0; j < n; j++) {
                row.add(-1);
            }
            board.add(row);
        }
        board.get(0).set(0, 0);
        if (solve(0, 0, 1)) {
            return board;
        }
        ArrayList<ArrayList<Integer>> noSol = new ArrayList<>();
        ArrayList<Integer> r = new ArrayList<>();
        r.add(-1);
        noSol.add(r);
        return noSol;
    }
    private boolean isSafe(int x, int y) {
        return (x >= 0 && y >= 0 && x < n && y < n && board.get(x).get(y) == -1);
    }
    private boolean solve(int x, int y, int step) {
        if (step == n * n) {
            return true;
        }
        for (int i = 0; i < 8; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (isSafe(nx, ny)) {
                board.get(nx).set(ny, step);
                if (solve(nx, ny, step + 1)) {
                    return true;
                }
                board.get(nx).set(ny, -1); 
            }
        }
        return false;
    }
}
