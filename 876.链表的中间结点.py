#
# @lc app=leetcode.cn id=876 lang=python3
#
# [876] 链表的中间结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # the second way:
        # slow and fast pointer
        # this way only need to loop the whole list once
        # each fast pointer moves two step, the slow pointer move one step
        # therefore, when the fast pointer arrive the end of list, the slow pointer is in the middle of list

        slow_pointer = head
        fast_pointer = head

        count = -1
        while fast_pointer is not None:
            count += 1
            if count % 2 == 0 and count != 0:
                slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next
            
        
        if count % 2 != 0:
            slow_pointer = slow_pointer.next

        return slow_pointer


        # # the first way
        # # set an anchor point each ten nodes
        # anchor_pool = list()

        # pointer = head
        # count = -1
        # while pointer is not None:
        #     count += 1
        #     if count % 10 == 0:             # 每10个node保存一个锚点
        #         anchor_pool.append(pointer)
        #     pointer = pointer.next
        
        # middle = (count+1) // 2             # 计算中位node的索引值
        # anchor_index = middle // 10
        # offset = middle % 10

        # pointer = anchor_pool[anchor_index] # 从临近的锚点开始查找中位node
        # for i in range(offset):
        #     pointer = pointer.next

        # return pointer

# @lc code=end

