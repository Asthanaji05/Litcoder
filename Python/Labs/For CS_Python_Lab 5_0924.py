"""
Pin generator task:
A personal identification number (PIN) is a numeric or alphanumeric password or
code used in the process of authenticating or identifying a user. 
The PIN numbers of the customers of FB Bank are encoded in an array. 
Your task is to decode the array and generate the six-digit PIN number based 
on the following rules:
1.Find the cumulative sum of all the digits until you get a single digit.
2.Replace all the odd numbers with their respective alphabets in lowercase 
i.e. 1=a, 2=b...9=i...
"""
import sys

def get_sum(num):
    """Recursive approach to get sum of digits until singular"""
    if num<9:
        return num
    dig, rem = num, 0
    num = 0
    while dig > 0:
        rem = dig%10
        dig = dig//10
        num += rem
    return get_sum(num)


def get_pin(arr):
    """
    Generate sum of digits and replace odd values with respective alphabets
    """
    result = []
    for item in arr:
        s = get_sum(item)
        if s%2==0:
            result.append(s)
        else:
            result.append(chr(96+s))
    return result
    
inputVal = map(int, input().split())
result = get_pin(inputVal)
print(''.join(map(str, result)))
                                                                                                                            