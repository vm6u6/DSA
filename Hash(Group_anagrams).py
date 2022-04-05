
def group_anagram( str ):
    L = len(str)
    sort_name = {}
    for i in range( L ):
        ### Below sectoin could be replaced by Hash Function
        tmp = sorted(str[i])
        join_name = ''
        for j in range( len(tmp) ):
            join_name = join_name + tmp[j]
        ###

        if join_name in sort_name:
            sort_name[join_name].append(str[i])
        else:
            sort_name[join_name] = [str[i]]

    return list(sort_name.values())
        
str = ["eat","tea","tan","ate","nat","bat"]
print( group_anagram(str) )
