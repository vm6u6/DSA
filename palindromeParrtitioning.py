
def partition(self, s: str):
        
        def palindrom( s ):
            if s == s[::-1]:
                return True
            else:
                return False

        def cal( s, res, tmp, cnt ):
            if cnt == len(s):
                res.append(tmp)
                return 
            for i in range( cnt,len(s) ):
                if palindrom( s[cnt:i+1] ) == True :  
                    cal( s, res, tmp + [s[cnt:i+1]], i+1 )

        def partition( s ):
            res = []
            tmp = []
            cnt = 0
            cal( s, res, tmp, cnt )
            return res
        
        return partition( s )

s = "cdd"
print(partition( s ))