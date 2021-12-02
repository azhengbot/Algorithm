
import java.util.*;

public class Solution77 {
    public List<List<Integer>> combine(int n, int k) {
        this.k = k;
        this.n = n;
        recur(1);
        return res;
    }

    int k;
    int n;
    List<List<Integer>> res = new ArrayList<>();
    List<Integer> subRes = new ArrayList<>();

    public void recur(int i) {
        if (i == n + 1) {
            if (subRes.size() == k) {
                res.add(new ArrayList<>(subRes));
            }
            return;
        }

        recur(i + 1);

        subRes.add(i);

        recur(i + 1);

        subRes.remove(subRes.size() - 1);

    }

    public static void main(String[] args) {
        Solution77 s = new Solution77();
        int n = 4;
        int k = 2;
        List<List<Integer>> res = s.combine(n, k);
        System.out.println(res);
    }
}
