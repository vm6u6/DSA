# def recur_decode( s, i, ans, tmp, num, num_tmp, num_len ):

#     if i >= len(s):
#         return s

#     elif s[i].isdigit():
#         num_tmp = num_tmp + s[i]

#     elif s[i] == "[":
#         ans = ans[:-1]
#         num.append( int(num_tmp) )
#         tmp.append(i+1)
#         num_len.append(len(num_tmp))   

#     elif s[i] == "]":
#         print(tmp)
#         print(s[:tmp[-1]-1-num_len[-1]])
#         print(s[tmp[-1]:i]*num[-1])
#         s = s[:tmp[-1]-1-num_len[-1]] + s[tmp[-1]:i]*num[-1] + s[i+1:]
       
#         tmp.pop()
#         num.pop()
#         num_len.pop()

#         if len(tmp) > 0:
#             i = tmp[-1]

#     return recur_decode( s, i+1, ans, tmp, num, num_tmp, num_len )
            
# i = 0; ans = ""; tmp = []; num = []; num_tmp =  ""; num_len = []
# print(recur_decode( s, i, ans, tmp, num, num_tmp, num_len ))

s = "3[a2[c]]"
# s = "3[a]2[bc]"
# s = "abc3[cd]xyz"
# s = "100[leetcode]"
