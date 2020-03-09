
import unittest


def knapsack(W, V, k):
    di = {}
    a = helper(W, V, k, len(W) - 1, di)
    return a


def helper(W, V, k, i, dp):
    if k <= 0:
        return 0
    if i == 0:
        if W[i] <= k:
            return V[i]
        return 0

    if (k, i) in dp:
        return dp[(k, i)]

    res = max(helper(W, V, k - W[i], i - 1, dp) + V[i], helper(W, V, k, i - 1, dp))
    dp[(k, i)] = res

    return res


def knapsack_bottom_up(W, V, k):
    n = len(W)
    dp = [[0] * (k + 1) for i in range(n)]

    for i in range(0, n):
        for j in range(k + 1):
            if j == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = max(dp[i - 1][j], (dp[i - 1][j - W[i]] if j - W[i] >= 0 else 0) + V[i])

    return dp[-1][-1]


class Test(unittest.TestCase):
    def test_knapsack(self):
        W = [1, 2, 3, 2, 5]
        V = [5, 3, 5, 3, 2]
        k = 10
        self.assertEqual(16, knapsack(W, V, k), "Should return maximum value we can store in knapsack")

        W = [1, 12, 3, 4, 5, 2, 10]
        V = [15, 3, 5, 3, 10, 5, 6]
        k = 20
        self.assertEqual(38, knapsack(W, V, k), "Should return maximum value we can store in knapsack")

        W = [10, 20, 30]
        V = [60, 100, 120]
        k = 50
        self.assertEqual(220, knapsack(W, V, k), "Should return maximum value we can store in knapsack")

    def test_knapsack_bottom_up(self):
        W = [1, 2, 3, 2, 5]
        V = [5, 3, 5, 3, 2]
        k = 10
        self.assertEqual(16, knapsack_bottom_up(W, V, k), "Should return maximum value we can store in knapsack")

        W = [1, 12, 3, 4, 5, 2, 10]
        V = [15, 3, 5, 3, 10, 5, 6]
        k = 20
        self.assertEqual(38, knapsack_bottom_up(W, V, k), "Should return maximum value we can store in knapsack")

        W = [10, 20, 30]
        V = [60, 100, 120]
        k = 50
        self.assertEqual(220, knapsack_bottom_up(W, V, k), "Should return maximum value we can store in knapsack")
