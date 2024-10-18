"""
Migratory Birds
to determine which type of plant is the most common, considering the list of 
sightings. You should print the ID number of the most common plant. If multiple 
types of plants are equally common, choose the plant with the smallest ID 
number.
"""
from collections import Counter

def get_max_freq(arr):
    """
    Function to calculate max frequency element with min id
    """
    freq = Counter(arr).items()
    #getting max freq value -> [1]
    max_freq = max(freq, key=lambda x: x[1])[1]
    #returning key of the freq with min among them - > [0]
    return min(filter(lambda x: x[1] == max_freq, freq))[0]
    
inputVal = list(map(int, input().split()))
result = get_max_freq(inputVal)
print(result)
                                                                                                                            