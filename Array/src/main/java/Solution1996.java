import java.util.Arrays;

public class Solution1996 {
    public int numberOfWeakCharacters(int[][] properties) {

        Arrays.sort(properties, (o1, o2) -> o1[0] != o2[0] ? o1[0] - o2[0] : o2[1] - o1[1]);

        int maxDef = 0;
        int ans = 0;
        for (int[] property : properties) {
            if (property[1] < maxDef) {
                ans++;
            } else {
                maxDef = property[1];
            }
        }

        return ans;
    }
}
