# 给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。

# 示例 1：
# 输入：head = [1,2,6,3,4,5,6], val = 6
# 输出：[1,2,3,4,5]

# 示例 2：
# 输入：head = [], val = 1
# 输出：[]

# 示例 3：
# 输入：head = [7,7,7,7], val = 7
# 输出：[]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeElements(head, val):
  while head and head.val == val:
    head = head.next

  pre, cur = head
  while cur:
    if cur.val == val:
      pre.next = cur.next
    else:
      pre = cur
    cur = cur.next

  return head


print(removeElements([1, 2, 6, 3, 4, 5, 6], 6))
print(removeElements([], 1))
print(removeElements([7, 7, 7, 7], 7))
