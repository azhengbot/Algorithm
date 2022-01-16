package week09;

import java.util.HashMap;

public class Solution387 {
    public int firstUniqChar(String s) {
        HashMap<Character, Integer> dict = new HashMap<>();

        for (char c : s.toCharArray()) {
            if (dict.containsKey(c)) {
                int count = dict.get(c);
                dict.put(c, ++count);
            } else {
                dict.put(c, 1);
            }
        }

        for (int i = 0; i < s.length(); i++) {

            if (dict.get(s.charAt(i)) == 1) {
                return i;
            }
        }
        return -1;
    }
}
