#
# @lc app=leetcode.cn id=2487 lang=python3
#
# [2487] 从链表中移除节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # 递归法 删除所有小于右侧节点值的节点
        # 递归遍历至链表尾部
        # 回溯，判断current_node(head)与next_node之间值的大小
        #   如果 current_node 小于 next_node, 则 return next_node，即删除current_node
        #   如果 current_node 不小于 next_node，则 return current_node
        def removeSmallerNode(head):
            if head.next == None:
                return head
            next_node = removeSmallerNode(head.next)
            if head.val < next_node.val:
                return next_node
            else:
                head.next = next_node
                return head
        
        return removeSmallerNode(head)


# @lc code=end

