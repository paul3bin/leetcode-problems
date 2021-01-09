"""Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. 
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is."""

# Difficulty: Hard

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head
        else:
            temp = head
            llist = []
            while temp:
                llist.append(temp.val)
                temp = temp.next
            if k<=len(llist):
                front_index, rear_index = 0, 0
                for i in range(len(llist)+1):
                    rear_index = i
                    if i%k==0:
                        llist[front_index:rear_index] = llist[front_index:rear_index][::-1]
                        front_index = rear_index
                
                tempHead = ListNode(0)
                result = [tempHead]
                for value in llist:
                    newNode = ListNode(value)
                    result[-1].next = newNode
                    result.append(newNode)
                return tempHead.next