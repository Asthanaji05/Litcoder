import sys
def max_chunks_to_sorted(arr):
    max_so_far = 0
    chunks = []
    chunk = []
    
    for i in range(len(arr)):
        max_so_far = max(max_so_far, arr[i])
        chunk.append(arr[i])
        
        if max_so_far == i:
            chunks.append(chunk)
            chunk = []
    
    return chunks

# Taking input in one line
arr = list(map(int, input().split()))

# Get chunks
chunks = max_chunks_to_sorted(arr)

# Printing chunks
for chunk in chunks:
    print(" ".join(map(str, chunk)))
