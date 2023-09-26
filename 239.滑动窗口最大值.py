#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # def get_top2(k_nums):
        #     top2 = [-10000] * 2
        #     for i in k_nums:
        #         if i > top2[0]:
        #             top2[0] = i
        #         elif i > top2[1]:
        #             top2[1] = i
        #     return top2
        
        import copy
        k_list = copy.copy(nums[:k])
        max_e = max(k_list)
        k_max = []
        k_max.append(max_e)
        for i in range(k, len(nums)):
            pop_e = k_list.pop(0)
            k_list.append(nums[i])
            if pop_e == max_e:
                max_e = max(k_list)
            k_max.append(max_e)
        
        return k_max

# @lc code=end

