mapping = { "2": "abc", "3": "def", "4": "ghi", 
            "5": "jkl", "6": "mno",  "7": "pqrs",  
            "8": "tuv",  "9": "wxyz"}

        
def recurse(index, mapping, currStr, digits, res):
    if len(digits) == 0: 
        return []

    if len(currStr) == len(digits): 
        res.append(currStr)
        return
    for i in range(index, len(digits)): 
        for char in mapping[digits[i]]: 
            recurse(i+1, mapping, currStr+char, digits, res)

digits = "23" 
res = []
recurse(0, mapping, "", digits, res)
print(res)


            
