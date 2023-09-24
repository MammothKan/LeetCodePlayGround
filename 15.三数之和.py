#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # 题目要求从数组nums中，找出三个不重复的数a，b，c，满足a+b+c=0
    
        # 哈希法
        # 1. 双层for循环遍历a和b，然后用哈希冲撞查找满足条件的c=0-a-b是否存在，时间复杂度O(n^2)
        # 2. 题目要求答案的三元组不可重复。所以第一步中获得的三元组，需要被再次去重
        # 此法，在leetcode中存在超时问题
        """
        result = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                a, b = nums[i], nums[j]
                _nums = nums[:i] + nums[i+1:j] + nums[j+1:]
                c = -(a + b)
                if c in _nums:
                    r = [a,b,c]
                    r.sort()
                    if r not in result:
                        result.append(r)
        return result 
        """

        # 双指针法
        # 在哈希法中，造成超时后的第一反应便是减值操作，即尽可能少的计算出重复的三元组
        # 1. 先对nums进行排序
        # 2. 通过for循环遍历 a，将a的下一个数值设置为b，将nums的最后一个数设置为c
        # 3. 由于nums已经升序排序，
        #       当 a+b+c > 0 时，将 c 向左移动，减小c的值
        #       当 a+b+c < 0 时，将 b 向右移动，增大b的值
        # 4. 当 index(b) >= index(c) 时，结束第3步的循环
        nums.sort()
        result = []
        for idx_a, a in enumerate(nums):
            # 减枝操作 a去重
            if idx_a > 0 and nums[idx_a-1] == a:
                continue
            left = idx_a + 1
            right = len(nums) - 1
            while left < right:
                b = nums[left]
                c = nums[right]
                # 减枝操作 c去重
                if right < (len(nums)-1) and nums[right+1] == c:
                    right -= 1
                    continue
                if a + b + c > 0:
                    right -= 1
                elif a + b + c < 0:
                    left += 1
                else:
                    result.append([a,b,c])
                    right -= 1      # 与 c去重的减枝操作 对应

        return result


# @lc code=end

