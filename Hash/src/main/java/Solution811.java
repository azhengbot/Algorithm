
import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;

public class Solution811 {
    public List<String> subdomainVisits(String[] cpdomains) {
        HashMap<String, Integer> resMap = new HashMap<>();

        for (String cpdomain : cpdomains) {
            String[] cpdomainInfo = cpdomain.split(" ");
            Integer count = Integer.valueOf(cpdomainInfo[0]);

            // Java 的split的参数是 正则
            String[] frags = cpdomainInfo[1].split("\\.");

            String domain = "";
            for (int i = frags.length - 1; i >= 0; i--) {
                domain = frags[i] + (i == frags.length - 1 ? "" : ".") + domain;
                resMap.put(domain, resMap.getOrDefault(domain, 0) + count);
            }

        }

        List<String> ans = new ArrayList<>();

        for (String key : resMap.keySet()) {
            String res = resMap.get(key) + " " + key;
            ans.add(res);

        }

        return ans;

    }

    public static void main(String[] args) {
        Solution811 s = new Solution811();
        String[] cpdomains = { "900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org" };

        List<String> res = s.subdomainVisits(cpdomains);

        System.out.println(res);
    }

}
