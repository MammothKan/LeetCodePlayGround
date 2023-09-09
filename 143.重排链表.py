#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # 双指针法 to get the center of the ListNode
        slow = head # step = 1
        fast = head # step = 2
        while  fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        right = slow.next         # the first node in the sequence that needs to be reordered is the next node to the centre node
        # left = head
        slow.next = None

        # 双指针法，利用递归
        def reorder(left, right):
            # 直到 right 走到最后一个node
            if right is None:
                return left, None
            left, _ = reorder(left, right.next)
            # 开始 做插入
            right.next = left.next
            left.next = right
            left = right.next
            return left, None
        
        reorder(head, right)

        return head

# @lc code=end

