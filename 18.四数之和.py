#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        # 双指针法
        # 此题的解法在 15.三数之和 上再添加一层循环
        # 1. 升序排序nums
        # 2. 双层for循环，遍历a和b，注意去重（减枝）
        # 3. 从b后一个开始，从两端，借助left和right搜索满足a+b+c+d=target的四元组
        # 4. 当 left >= right 时，结束第3步中的循环
        result = []
        nums.sort()
        for idx_a in range(len(nums)):
            a = nums[idx_a]
            if idx_a > 0 and a == nums[idx_a-1]:
                continue            # 去重 a
            for idx_b in range(idx_a+1, len(nums)):
                b = nums[idx_b]
                if idx_b > idx_a+1 and b == nums[idx_b-1]:
                    continue        # 去重 b
                left, right = idx_b+1, len(nums)-1  # idx_c; idx_d
                while left < right:
                    c = nums[left]
                    d = nums[right]
                    if right < len(nums)-1 and d == nums[right+1]:
                        right -= 1
                        continue    # 去重 d
                    if a+b+c+d > target:
                        right -= 1
                    elif a+b+c+d < target:
                        left += 1
                    else:
                        result.append([a,b,c,d])
                        right -= 1  # 与去重d对应
        return result

# @lc code=end

