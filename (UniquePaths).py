class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        total = m + n - 1 
        ans = 1
        tmp1 = 1
        tmp2 = 1
        for i in range( 1, total ):
            ans = ans * i
        for i in range( 1, m ):
            tmp1 = tmp1 * i
        for i in range( 1, n ):
            tmp2 = tmp2 * i
        
        ans = (ans// tmp1)//tmp2
        return ans