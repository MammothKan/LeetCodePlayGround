#
# @lc app=leetcode.cn id=805 lang=python3
#
# [805] 数组的均值分割
#

# @lc code=start
import itertools


class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:

        if len(nums) == 1:
            return False
        elif len(nums) == 2:
            if nums[0] == nums[1]:
                return True
            else:
                return False

        n_nums = list()
        for i in nums:
            n_nums.append(i*len(nums))
        aver = sum(n_nums) / len(n_nums)
        zero_nums = list()
        for i in n_nums:
            zero_nums.append(i - aver)
        
        a_list = zero_nums[0:int(len(nums)/2)]
        b_list = zero_nums[int(len(nums)/2):]

        # print(a_list)
        # print(b_list)

        a_subsets = dict()
        for i in range(0, len(a_list)+1):
            for subset in itertools.combinations(a_list, i):
                a_subsets[subset] = sum(list(subset))
        a_subsets =  sorted(a_subsets.items(), key=lambda x: x[1])

        b_subsets = dict()
        for i in range(0, len(b_list)+1):
            for subset in itertools.combinations(b_list, i):
                b_subsets[subset] = sum(list(subset))
        b_subsets =  sorted(b_subsets.items(), key=lambda x: x[1], reverse=True)
        
        # print(a_subsets)
        # print(b_subsets)

        for a_subset_sum in a_subsets:
            for b_subnet_sum in b_subsets:
                if a_subset_sum[1] == - b_subnet_sum[1] and len(a_subset_sum[0]) + len(b_subnet_sum[0]) < len(nums) and len(a_subset_sum[0]) + len(b_subnet_sum[0]) > 0:
                    return True
                elif a_subset_sum[1] < -b_subnet_sum[1]:
                    continue
        
        return False




# @lc code=end