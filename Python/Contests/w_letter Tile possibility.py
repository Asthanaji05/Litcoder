import sys
from itertools import permutations
def num_tile_possibilities(tiles):
    unique_sequences = set()
    
    # Generate all permutations for different lengths
    for i in range(1, len(tiles) + 1):
        for perm in permutations(tiles, i):
            unique_sequences.add(perm)
    return len(unique_sequences)

inputVal = input()
print(num_tile_possibilities(inputVal))