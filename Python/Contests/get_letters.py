"""
Phone no to letters
"""


def get_letters(digits):
    d = {
        '2' : "abc",
        '3' : "def",
        '4' : "ghi",
        '5' : "jkl",
        '6' : "mno",
        '7' : "pqrs",
        '8' : "tuv",
        '9' : "wxyz"}
        
    #Removing characters other than in the dict keys
    digits = ''.join(list(filter(lambda x: x in d.keys(), digits)))
    print(digits)
        
    result = []
    if not digits: return result
    
    def backtrack(n, s=""):
        if not n:
            result.append(s)
            return 
        for a in d[n[0]]:
            s+=a
            backtrack(n[1:], s)
            s=s[:-1]
    backtrack(digits)
    return result

inputVal = input()
print(' '.join(get_letters(inputVal)))