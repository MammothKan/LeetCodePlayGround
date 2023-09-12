#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def print_list(head):
            if head == None: print('None')
            while head != None:
                print(head.val, sep='->')
                head = head.next

        # 非递归法：新造链表法
        # import copy
        # float_point = ListNode()
        # newhead = float_point

        # p = None
        # n = None
        # while head != None:
        #     p = copy.copy(head)
        #     n = copy.copy(head.next)
        #     if n != None:
        #         p.next, n.next = None, None
        #         float_point.next = n
        #         float_point.next.next = p
        #         float_point = float_point.next.next
        #         head = head.next.next
        #     else:
        #         p.next = None
        #         float_point.next = p
        #         head = head.next
            
        # return newhead.next


        # 递归法
        def swap(head):
            if head == None or head.next == None:
                return head
            head_of_next_pair = swap(head.next.next)
            next_head = head.next
            next_head.next = head
            head.next = head_of_next_pair
            return next_head
        
        return swap(head)
                 


# @lc code=end

