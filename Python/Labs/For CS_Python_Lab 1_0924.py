import sys
def doSomething(inval):
    #Do Something
    n = list(map(int, inval.split()))
    neg, zero, pos = [], [], []
    
    for i in n:
        if i < 0:
            neg.append(i)
        elif i == 0:
            zero.append(i)
        else:
            pos.append(i)
    
    outval = '\n'.join(map(lambda x: "{:.3f}".format(len(x)/len(n)), [pos, neg, zero]))
    return outval
n = input()
inputVal = input()    
outputVal = doSomething(inputVal)
print (outputVal)
                                                                                                                            