#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # hashtable = {}
        # for i, n in enumerate(nums):
        #     hashtable[n] = hashtable.get(n, [])
        #     hashtable[n].append(i)
        # # print(hashtable)

        # result = []
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         a, b = nums[i], nums[j]
        #         # remove
        #         hashtable[a].remove(i)
        #         hashtable[b].remove(j)
        #         # 
        #         c = -(a + b)
        #         if c in hashtable and len(hashtable[c])>0:
        #             # for idx_c in hashtable[c]:
        #                 # result.append([i,j,idx_c])
        #             r = [a,b,c]
        #             r.sort()
        #             # print(r)
        #             if r not in result:
        #                 result.append(r)
                
        #         # reset
        #         hashtable[a].append(i)
        #         hashtable[b].append(j)
        # # print(result)

        # return result 
    

        # result = []
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         a, b = nums[i], nums[j]
        #         _nums = nums[:i] + nums[i+1:j] + nums[j+1:]
                
        #         c = -(a + b)
        #         if c in _nums:
        #             r = [a,b,c]
        #             r.sort()
        #             if r not in result:
        #                 result.append(r)

        # return result 


        nums.sort()
        result = []
        for idx_a, a in enumerate(nums):
            if idx_a > 0 and nums[idx_a-1] == a:
                continue
            left = idx_a + 1
            right = len(nums) - 1
            while left < right:
                b = nums[left]
                c = nums[right]
                if a + b + c > 0:
                    right -= 1
                elif a + b + c < 0:
                    left += 1
                else:
                    result.append([a,b,c])
                    # break
                    right -= 1

        
        return result




# @lc code=end

