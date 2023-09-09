#
# @lc app=leetcode.cn id=2681 lang=python3
#
# [2681] 英雄的力量
#

# @lc code=start
class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        # 冒泡排序
        # for i in range(len(nums)-1, 0, -1):
        #     for j in range(0,i):
        #         if nums[j] > nums[j+1]:
        #             _num = nums[j+1]
        #             nums[j+1] = nums[j]
        #             nums[j] = _num

        nums.sort()
        dp = [0 for i in range(len(nums))]
        pre_sum = [0 for i in range(len(nums) + 1)]
        res, mod = 0, 10 ** 9 + 7
        for i in range(len(nums)):
            dp[i] = (nums[i] + pre_sum[i]) % mod
            pre_sum[i + 1] = (pre_sum[i] + dp[i]) % mod
            res = (res + nums[i] * nums[i] * dp[i]) % mod
        return res



                

# @lc code=end

