class Solution:
    def rob(self, nums) -> int:
        # for each house we decide rob or not rob it. We need to look back if last house was robbed or not to rob current house, if we decide to rob current house then update max robbed money and robbed_moneys
        # robbed_moneys[0] - total robbeb money
        # robbed_moneys[1] - was last house robbed?
        robbed_moneys = [[0, 0]]
        res = 0

        for i in range(len(nums)):
            n = len(robbed_moneys)
            for i in range(n):
                robbed_money = robbed_moneys[i]

                if not robbed_money[1]:
                    new_robbed_money = robbed_money[0] + nums[i]
                    res = max(res, new_robbed_money)
                    robbed_moneys.append([new_robbed_money, 1])
                else:
                    # not rob current house so update r1 to 0
                    robbed_money[1] = 0

        return res

s = Solution()
nums = [2,7,9,3,1]

print(s.rob(nums))