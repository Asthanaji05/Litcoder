import sys

def max_difficulty(diffs, times, queries):
    sorted_diffs_on_time = [x for _, x in sorted(zip(times, diffs), reverse=True)]
    return '\n'.join(list(str(sum(sorted_diffs_on_time[:q])) for q in queries))

output = max_difficulty(list(map(int, input().split())), 
list(map(int, input().split())), 
list(map(int, input().split())))
print(output)