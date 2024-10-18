"""
A special prime number is a unique type of prime number that can be constructed 
by concatenating its individual digits in a particular order. The resulting 
numbers, obtained by considering all possible combinations of concatenation, 
must also be prime.
"""

import sys
    
def simple_sieve(n):
    """
    To generate all primes up to n
    """
    arr = [True] * (n)
    arr[0], arr[1] = False, False
    for i, p in enumerate(arr):
        if p:
            for j in range(i+i, n, i):
                arr[j] = False
                
    primes = []
    for i, el in enumerate(arr):
        if el:
            primes.append(i)
    return primes
    
def is_special(n, primes):
    """
    Check for a prime is special or not"
    """
    dig = str(n)
    for i in range(len(dig)):
        if int(dig[:i+1]) not in primes:
            return False
    return True

def special_prime(primes):
    """
    To check each prime if it is a special prime
    """
    for i in primes:
        if is_special(i, primes):
            return i

        
inputVal = int(input())
primes = sorted(simple_sieve(inputVal), reverse=True)
special = special_prime(primes)
print(special)
                                                                                                                            