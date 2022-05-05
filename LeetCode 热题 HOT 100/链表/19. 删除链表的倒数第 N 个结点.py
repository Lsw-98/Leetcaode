# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。 

# 示例 1：
# 输入：head = [1, 2, 3, 4, 5], n = 2
# 输出：[1, 2, 3, 5]

# 示例 2：
# 输入：head = [1], n = 1
# 输出：[]

# 示例 3：
# 输入：head = [1, 2], n = 1
# 输出：[1]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(head, n):
        if not head:
            return

        for _ in range(n - 1):
            head = head.next
        head = head.next.next
        return head
