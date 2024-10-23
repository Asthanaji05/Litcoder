"""
Check Panagram
"""

def is_pangram(s):
    """
    Checking freq of of each letter
    """
    s = s.upper()
    d = dict.fromkeys([chr(i+65) for i in range(26)], 0)
    for i in s:
        d[i] = d.get(i, 0) + 1
    return list(d.values()).count(0) == 0

inputVal = input()
print("pangram" if is_pangram(inputVal) else "not a pangram")