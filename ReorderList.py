# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
  
        def getlast( head ):
            if head.next == None:
                return head
            else:
                return getlast( head.next )
            
        def poplast ( head ):
            if head.next.next == None:
                head.next = None
                return
            else:
                poplast( head.next )
            return head.next
                
        
        def reorder( head, cnt ):
            if head.next.next == None:
                return head
            
            if cnt == 1:
                last_node = getlast( head )
                residule_next = poplast( head )

                head.next = None
                last_node.next =  residule_next
                head.next = last_node

                return reorder( head.next, cnt = 0 )
            elif cnt == 0:

                return reorder( head.next, cnt = 1 )
            
        pre = None
        cnt = 1 # for the last
        if head == None:
            return head
        if head.next == None:
            return head
        return reorder( head, cnt )