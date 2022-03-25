import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

public class Solution49 {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> resMap = new HashMap<>();
        for (String str : strs) {
            char[] chars = str.toCharArray();
            Arrays.sort(chars);
            String key = new String(chars);
            List<String> strings = resMap.getOrDefault(key, new ArrayList<String>());
            strings.add(str);
            resMap.put(key, strings);
        }
        return new ArrayList<List<String>>(resMap.values());
    }
}
