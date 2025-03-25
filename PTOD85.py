class Solution:
    def countWays(self, s):
        dp = {}  
        def solve(i, j, isTrue):
            if i > j:
                return 0  
            if i == j:
                if isTrue:
                    return 1 if s[i] == 'T' else 0
                else:
                    return 1 if s[i] == 'F' else 0
            if (i, j, isTrue) in dp:
                return dp[(i, j, isTrue)]
            ways = 0
            for k in range(i + 1, j, 2):  
                leftTrue = solve(i, k - 1, True)
                leftFalse = solve(i, k - 1, False)
                rightTrue = solve(k + 1, j, True)
                rightFalse = solve(k + 1, j, False)
                if s[k] == '&':
                    if isTrue:
                        ways += leftTrue * rightTrue
                    else:
                        ways += leftTrue * rightFalse + leftFalse * rightTrue + leftFalse * rightFalse
                elif s[k] == '|':
                    if isTrue:
                        ways += leftTrue * rightTrue + leftTrue * rightFalse + leftFalse * rightTrue
                    else:
                        ways += leftFalse * rightFalse
                elif s[k] == '^':
                    if isTrue:
                        ways += leftTrue * rightFalse + leftFalse * rightTrue
                    else:
                        ways += leftTrue * rightTrue + leftFalse * rightFalse
            dp[(i, j, isTrue)] = ways
            return ways
        return solve(0, len(s) - 1, True)
sol = Solution()
