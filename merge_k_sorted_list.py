"""You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it."""

# Difficulty: Hard

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        temp = []
        for llist in lists:
            t = llist
            while t:
                temp.append(t.val)
                t = t.next
        
        head = ListNode(0)
        sorted_list = [head]
        temp.sort()
        for value in temp:
            newNode = ListNode(value)
            sorted_list[-1].next = newNode
            sorted_list.append(newNode)
        return head.next