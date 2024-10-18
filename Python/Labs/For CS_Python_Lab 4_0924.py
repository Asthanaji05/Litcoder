import sys

def doSomething(inval):
    #Do Something
    inval = list(map(lambda x: str((int(x)+5)%10), list(inval)))
    inval[0], inval[1] ,inval[2], inval[3] = inval[2], inval[3], inval[0], inval[1]
        
    return ''.join(inval)

input = input()
#input = int(input())
output = doSomething(input)
print (output)
                                                                                                                            