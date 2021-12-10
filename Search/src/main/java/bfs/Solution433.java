package bfs;

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Queue;

public class Solution433 {
    public int minMutation(String start, String end, String[] bank) {
        char[] genes = { 'A', 'C', 'G', 'T' };
        HashMap<String, Integer> depth = new HashMap<>();

        HashSet<String> bankSet = new HashSet<>(Arrays.asList(bank));
        Queue<String> q = new ArrayDeque<>();

        if (!bankSet.contains(end)) {
            return -1;
        }

        depth.put(start, 0);
        q.add(start);

        while (!q.isEmpty()) {
            String first = q.poll();

            for (int i = 0; i < 8; i++) {
                for (char gene : genes) {
                    if (first.charAt(i) == gene) {
                        continue;
                    }
                    String newFirst = first.substring(0, i) + gene + first.substring(i + 1, first.length());

                    if (!bankSet.contains(newFirst)) {
                        continue;
                    }
                    if (depth.containsKey(newFirst)) {
                        continue;
                    }

                    depth.put(newFirst, depth.getOrDefault(first, 0) + 1);

                    q.add(newFirst);

                    if (newFirst.equals(end)) {
                        return depth.get(newFirst);
                    }
                }
            }

        }

        return -1;

    }

    public static void main(String[] args) {
        Solution433 s = new Solution433();

        String start = "AACCGGTT";
        String end = "AAACGGTA";
        String[] bank = { "AACCGGTA", "AACCGCTA", "AAACGGTA" };
        int res = s.minMutation(start, end, bank);
        System.out.print(res);

    }
}
