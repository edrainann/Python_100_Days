# -*- coding: utf-8 -*-
# @Time    : 2020/4/29
# @Author  : Edrain
"""
21. 合并两个有序链表
将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def printList(head):
    cur = head
    while cur != None:
        print(cur.val, '-->', end='')
        cur = cur.next
    print('NULL')

class SingleLinkList(object):
    """单链表"""
    def __init__(self):
        self._head = None

    def add(self, val):
        """向链表头部添加元素"""
        node = ListNode(val)
        # 新结点指针指向原头部结点
        node.next = self._head
        # 头部结点指针修改为新结点
        self._head = node

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
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
        return ListNode(6)


if __name__ == '__main__':
    """
    # 创建链表
    link_list = SingleLinkList()
    # 创建节点
    node11 = ListNode(1)
    node12 = ListNode(2)
    # 将节点添加到列表
    link_list._head = node11
    node11.next = node12
    # 将节点添加到列表
    link_list.add(9)
    link_list.add(8)
    print(link_list._head.val)
    print(link_list._head.next.val)
    print(link_list)
    """
    link_list1 = ListNode(1)
    link_list1_tail = link_list1
    link_list1_tail.next = ListNode(2)
    link_list1_tail = link_list1
    print("---", link_list1_tail)
    print("---", link_list1_tail.val)
    printList(link_list1_tail)

    ln = ListNode(8)
    so = Solution()
    ml1 = [4]
    ml2 = [1]
    # ln1 = ListNode()
    ln1 = ListNode(2)
    ln2 = ListNode(4)
    print(so.mergeTwoLists(ln1, ln2))
    # print(so.mergeTwoLists(ml1, ml2))
