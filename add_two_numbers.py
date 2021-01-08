"""You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself."""

# Difficulty: Medium

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp1, temp2 = l1, l2
        s1,s2 = '', ''
        
        while(temp1):
            s1 += str(temp1.val)
            temp1 = temp1.next
            
        while(temp2):
            s2 += str(temp2.val)
            temp2 = temp2.next
            
        
        summ = int(s1[::-1]) + int(s2[::-1])
        sumList = list(str(summ)[::-1])
        head = ListNode(0)
        result_list = [head]
        for value in sumList:
            newNode = ListNode(value)
            result_list[-1].next = newNode
            result_list.append(newNode)
        return head.next