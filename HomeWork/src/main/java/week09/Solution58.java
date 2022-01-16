package week09;

public class Solution58 {
    public int lengthOfLastWord(String s) {
        String[] sList = s.split(" ");
        int n = sList.length;

        for (int i = n - 1; i >= 0; i--) {
            if (!sList[i].equals(" ")) {
                return sList[i].length();
            }
        }

        return 0;

    }
}
