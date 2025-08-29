class Solution {
    public static String smallestWindow(String s, String p) {
        int n = s.length(), m = p.length();
        Map<Character, Integer> desiredFreq = new HashMap<>();
        Map<Character, Integer> currFreq = new HashMap<>();
        for (int i = 0; i < m; i++) {
            desiredFreq.put(p.charAt(i), desiredFreq.getOrDefault(p.charAt(i), 0) + 1);
        }
        int start = -1, end = -1;
        int l = 0;
        for (int r = 0; r < n; r++) {
            if (desiredFreq.containsKey(s.charAt(r))) {
                currFreq.put(s.charAt(r), currFreq.getOrDefault(s.charAt(r), 0) + 1);
            }
            while (l <= r && isValidSubstring(currFreq, desiredFreq)) {
                if (start == -1 || r - l + 1 < end - start + 1) {
                    start = l;
                    end = r;
                }
                if (desiredFreq.containsKey(s.charAt(l))) {
                    currFreq.put(s.charAt(l), currFreq.get(s.charAt(l)) - 1);
                }
                l++;
            }
        }
        return start == -1 ? "" : s.substring(start, end + 1);
    }
    private static boolean isValidSubstring(Map<Character, Integer> currFreq, Map<Character, Integer> desiredFreq) {
        for (var entry : desiredFreq.entrySet()) {
            char dkey = entry.getKey();
            int dvalue = entry.getValue();
            if (currFreq.getOrDefault(dkey, 0) < dvalue) {
                return false;
            }
        }
        return true;
    }
}
