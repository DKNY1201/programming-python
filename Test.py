def numRollsToTarget(d: int, f: int, target: int) -> int:
    dp = [[0] * (target + 1) for i in range(d + 1)]

    for i in range(1, d + 1):
        for j in range(target + 1):
            if j == 0:
                dp[i][j] = 0
            elif i == 1:
                if j <= f:
                    dp[i][j] = 1
            else:
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1] - (dp[i - 1][j - f - 1] if j > f else 0)

    return dp[d][target]

print(numRollsToTarget(4,6,10))