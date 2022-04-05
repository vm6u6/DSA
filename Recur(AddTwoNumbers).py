class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        
        nums = ListNode(0)
        Ans = nums
        dec = 0
        while l1 is not None or l2 is not None or dec > 0:
        
            if ( l1 is not None ):
                l1val = l1.val
            else:
                l1val = 0

            if ( l2 is not None ):
                l2val = l2.val
            else:
                l2val = 0

            val = l1val + l2val + dec
            if ( val >= 10 ):
                dec = 1
            else:
                dec = 0
            Ans.next = ListNode(val%10)
            
            Ans = Ans.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        return nums.next

