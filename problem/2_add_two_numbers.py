"""
Copyright (c) College of Mechatronics and Control Engineering, Shenzhen University.
All rights reserved.

Description :


Author：Team Li
"""

"""
2. Add Two Numbers
Medium

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    ## time O(n), but code not beautiful...
    def sub_add(node, extra_add, l1_node, l2_node):
        """
        Args:
            node: a new node, which would be used to store the l1_node.val + l2_node.val + extra_add
            extra_add: indicate last add whether bigger than 10
            l1_node: current node of l1
            l2_node: current node of l2
        """
        if l1_node or l2_node:
            if not l1_node:
                l1_val = 0
            else:
                l1_val = l1_node.val
            if not l2_node:
                l2_val = 0
            else:
                l2_val = l2_node.val

            node.val = (l1_val + l2_val) % 10 + extra_add

            if (l1_val + l2_val) >= 10:
                extra_add = 1
            else:
                extra_add = 0

            if node.val >= 10:
                node.val %= 10
                extra_add = 1

            if not l2_node:
                if l1_node.next:
                    new_node = ListNode(0)
                    node.next = new_node
                    sub_add(new_node, extra_add, l1_node.next, l2_node)
                elif extra_add:
                    new_node = ListNode(0)
                    node.next = new_node
                    sub_add(new_node, extra_add, l1_node.next, l2_node)
            elif not l1_node:
                if l2_node.next:
                    new_node = ListNode(0)
                    node.next = new_node
                    sub_add(new_node, extra_add, l1_node, l2_node.next)
                elif extra_add:
                    new_node = ListNode(0)
                    node.next = new_node
                    sub_add(new_node, extra_add, l1_node, l2_node.next)
            else:
                if not l1_node.next and not l2_node.next:
                    if extra_add:
                        new_node = ListNode(0)
                        node.next = new_node
                        sub_add(new_node, extra_add, l1_node.next, l2_node.next)
                else:
                    new_node = ListNode(0)
                    node.next = new_node
                    sub_add(new_node, extra_add, l1_node.next, l2_node.next)
        elif not l1_node and not l2_node:
            if extra_add:
                node.val = 1

    new_head = ListNode(0)
    sub_add(new_head, 0, l1, l2)
    return new_head