# max length is 3 
# ID must in 0 ~ 255

def backtrack ( s, tmp, num, ans, idx ):
    L = len(s)
    
    val = int(num)
    if val > 255 or val < 0 :
        return


    if idx == len(s):
        ans.append( tmp )

    backtrack ( s, tmp, )
    



s = "25525511135"
num = ""; tmp = ""; ans = []; idx = 0
backtrack ( s, tmp, num, ans, idx )