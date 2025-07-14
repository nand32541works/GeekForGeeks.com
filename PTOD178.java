import java.util.HashSet;
import java.util.Set;

class Solution {
    private static final Set<String> powersOfFive = new HashSet<>();
    static {
        long num = 1;
        while (num <= (1L << 30)) {
            powersOfFive.add(Long.toBinaryString(num));
            num *= 5;
        }
    }
    public int cuts(String s) {
        int n = s.length();
        int[] dp = new int[n + 1];
        dp[0] = 0; 
        for (int i = 1; i <= n; i++) {
            dp[i] = Integer.MAX_VALUE;
            for (int j = 0; j < i; j++) {
                String sub = s.substring(j, i);
                if (sub.charAt(0) != '0' && powersOfFive.contains(sub)) {
                    if (dp[j] != Integer.MAX_VALUE) {
                        dp[i] = Math.min(dp[i], dp[j] + 1);
                    }
                }
            }
        }
        return dp[n] == Integer.MAX_VALUE ? -1 : dp[n];
    }
}
