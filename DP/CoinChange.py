"""
https://leetcode.com/problems/coin-change/
"""
import unittest


def coin_change(coins, total):
    memo = [0] * (total + 1)

    return helper(coins, total, memo)


def helper(coins, total, memo):
    if total == 0:
        return 0

    if memo[total]:
        return memo[total]

    min_coins = float("Inf")

    for coin in coins:
        # no need to run when total less than coin value
        if total >= coin:
            # get recursive min coins
            min_coins_res = helper(coins, total - coin, memo)
            # ignore if recursive coins can't make the change
            if min_coins_res >= 0:
                # get the minimum recursive coins + 1
                min_coins = min(min_coins, min_coins_res) + 1

    memo[total] = -1 if min_coins == float("Inf") else min_coins

    return memo[total]


class Test(unittest.TestCase):
    def test_coin_change(self):
        coins = [1, 2, 5]
        amount = 11
        self.assertEqual(3, coin_change(coins, amount), "Should minimum number of coins that can make the change")

        coins = [2]
        amount = 3
        self.assertEqual(-1, coin_change(coins, amount), "Should return -1 if can not make the change")