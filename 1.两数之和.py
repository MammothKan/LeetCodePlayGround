#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # 哈希法
        # 先从nums随机选一个正整数a，计算b=target-a，然后借助哈希法查找b是否在nums中
        # 时间复杂度 O(n)
        for a_idx in range(len(nums)):
            b = target - nums[a_idx]
            b_list = nums[:a_idx]
            b_list.extend(nums[a_idx+1:])
            if b in b_list:
                b_idx = b_list.index(b)
                b_idx = b_idx if b_idx < a_idx else b_idx+1
                break
            else:
                continue

        return [a_idx, b_idx]

# @lc code=end

