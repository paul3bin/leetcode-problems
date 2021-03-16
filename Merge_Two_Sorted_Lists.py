"""Merge two sorted linked lists and return it as a sorted list. 
The list should be made by splicing together the nodes of the first two lists."""

# Difficulty: Easy

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp1, temp2 = l1, l2
        temp_llist1, temp_llist2 = [], []

        while temp1 or temp2:
            if temp1:
                temp_llist1.append(temp1.val)
                temp1 = temp1.next
            if temp2:
                temp_llist2.append(temp2.val)
                temp2 = temp2.next

        final_list = temp_llist1+temp_llist2
        final_list.sort()
        head = ListNode(0)
        result = [head]
        for value in final_list:
            newNode = ListNode(value)
            result[-1].next = newNode
            result.append(newNode)
        return head.next
