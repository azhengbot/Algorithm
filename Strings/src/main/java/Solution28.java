
public class Solution28 {
    public int strStr(String haystack, String needle) {
        long b = 131L;
        long p = (long) (1e9 + 7);

        int m = haystack.length();
        int n = needle.length();

        long[] hayHash = new long[m + 1];

        for (int i = 1; i < m + 1; i++) {
            hayHash[i] = (long) (hayHash[i - 1] * b + haystack.charAt(i - 1) - 'a' + 1) % p;
        }

        long neeHash = 0;
        long powBM = 1;
        for (int i = 0; i < n; i++) {
            neeHash = (long) (neeHash * b + needle.charAt(i) - 'a' + 1) % p;
            powBM = powBM * b % p;
        }

        // List<Long> s = Arrays.stream(hayHash).boxed().collect(Collectors.toList());

        for (int left = 1; left <= m + 1 - n; left++) {
            int right = left + n - 1;

            // long subHayHash = ((hayHash[right] - (hayHash[left - 1] * (long) Math.pow(b,
            // n))) % p + p) % p;
            // System.out.println((long) Math.pow((b % p), n));
            // System.out.println(powBM);
            long subHayHash = ((hayHash[right] - hayHash[left - 1] * powBM) % p + p) % p;

            if (neeHash == subHayHash) {
                return left - 1;
            }

        }

        return -1;
    }

    public static void main(String[] args) {
        Solution28 s = new Solution28();
        // String a = "mississippi";
        // String b = "issi";

        // String a = "mississippi";
        // String b = "sippi";

        String a = "aabaaabaaac";
        String b = "aabaaac";

        int res = s.strStr(a, b);
        System.out.println(res);
    }
}
