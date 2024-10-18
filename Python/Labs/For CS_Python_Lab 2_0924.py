import sys

def doSomething(inputhrs, inputdev):
    #Do Something
    if inputhrs <= 4:
        return "Invalid Input"
        
    devices = inputhrs//4
    if devices <= inputdev:
        return f"{devices}\n{inputdev-devices}"
    else:
        return f"{inputdev}\n0"
    

inputhrs = int(input())
inputdev = int(input())
output = doSomething(inputhrs, inputdev)
print (output)
                                                                                                                            