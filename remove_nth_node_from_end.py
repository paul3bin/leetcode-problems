'''
Given the head of a linked list, 
remove the nth node from the end of the list and return its head.
'''

# Difficulty: Medium

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp = head
        temp_list = []
        while temp:
            temp_list.append(temp.val)
            temp = temp.next
        temp_list.pop(-n)
        head = ListNode(0)
        prev = head
        for value in temp_list:
            newNode = ListNode(value)
            prev.next = newNode
            prev = newNode
        return head.next
