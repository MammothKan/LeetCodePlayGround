#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        current_node = head
        had_nodes = dict()
        while True:
            if current_node not in had_nodes:
                had_nodes[current_node] = current_node.val
            if current_node.next == None:
                return False
            
            next_node = current_node.next
            if next_node in had_nodes:
                return True
            current_node = next_node

        
# @lc code=end

