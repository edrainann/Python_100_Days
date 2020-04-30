# -*- coding: utf-8 -*-
# @Time    : 2020/4/30
# @Author  : Edrain


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """合并有序链表"""
        current = dummy = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        current.next = l1 or l2
        return dummy.next


def creat_link_list1():
    """创建link list1"""
    head = ListNode(0)
    cur = head
    cur.next = ListNode(1)
    cur.next.next = ListNode(2)
    cur.next.next.next = ListNode(7)
    return head


def creat_link_list2():
    """创建link list2"""
    head = ListNode(1)
    cur = head
    cur.next = ListNode(3)
    cur.next.next = ListNode(4)
    cur.next.next.next = ListNode(5)
    return head


def print_list(head):
    """输出link list"""
    cur = head
    while cur is not None:
        print(cur.val, '-->', end='')
        cur = cur.next
    print('NULL')


if __name__ == "__main__":
    l1 = creat_link_list1()
    print_list(l1)
    l2 = creat_link_list2()
    print_list(l2)
    result_link_list = Solution().merge_two_lists(l1, l2)
    print_list(result_link_list)
