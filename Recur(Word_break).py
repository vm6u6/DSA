
def word_break( s, d, ans ):

    if len(s) == 0:
        print(ans)
        return
    if len(s) == 1 and len(ans) > 0:
        print(ans)
        return

    for i in range( 1, len(s)+1 ):
        tmp = s[:i]
        #match
        if tmp in d:
            if ans == "":
                ans = tmp
            else:
                ans = ans + " " + tmp
            word_break( s[i:], d, ans ) 

def word_break2( s, d , i , j, ans):
    if j > len(s):    
        print(ans)
        return
    else:
        if s[i:j] in d:
            tmp = s[i:j]
            ori = ans
            if ans == "":
                ans = tmp
            else:
                ans = ans + " " + tmp
            word_break2(s, d, j, j+1, ans)
            if j < len(s):
                word_break2(s, d, i, j+1, ori)
        elif ans == "":        
            word_break2(s, d, i, j+1, ans)
    return


if __name__ == '__main__':
    d = { "this", "th", "is", "famous", "Word", "break", "b", "r", "e", "a", "k", "br", "bre", "brea", "ak", "problem" }
    s = "Wordbreakpeobkem"
    ans =""
    i = 0
    j = 1
    #word_break( s, d, ans )
    word_break2( s, d, i, j, ans )