#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # set a dummy node

        # This way is helpful to make the manage of 
        # list‘s the first node, because the real 
        # first node is replaced by a dummy node.

        # In this programme, if we do not use the 
        # dummy node, we have to add an additional 
        # codes to define the first node of merged list:
        # 
            # if l1_pointer.val <= l2_pointer.val:
            #     head = ListNode(val=l1_pointer.val)
            #     l1_pointer = l1_pointer.next
            # else:
            #     head = ListNode(val=l2_pointer.val)
            #     l2_pointer = l2_pointer.next
            # the next node
        #

        dummy = ListNode(val=-1)    # set a dummy node
        current_pointer = dummy
        l1_pointer = list1
        l2_pointer = list2
        while l1_pointer is not None and l2_pointer is not None:
            if l1_pointer.val <= l2_pointer.val:
                current_pointer.next = ListNode(val=l1_pointer.val)
                l1_pointer = l1_pointer.next
            else:
                current_pointer.next = ListNode(val=l2_pointer.val)
                l2_pointer = l2_pointer.next
            current_pointer = current_pointer.next
        # for tail nodes and the empty list
        if l1_pointer is not None:
            current_pointer.next = l1_pointer
        elif l2_pointer is not None:
            current_pointer.next = l2_pointer

        return dummy.next           # avoid the dummy node

# @lc code=end

