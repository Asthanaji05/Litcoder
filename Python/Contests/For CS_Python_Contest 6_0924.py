"""
job sequencing
"""

def get_job_schedule(n, name, dl, profit):
    day_profit = {}
    res = ['']*n
    for i, day in enumerate(dl):
        if profit[i] > day_profit.get(day, 0):
            day_profit[day] = profit[i]
            res[day-1] = arr[i]# since its 1 indexed
        
    return ' '.join(res)

n = int(input())
arr = input().split()
dl = list(map(int, input().split()))
p = list(map(int, input().split()))
print(get_job_schedule(n, arr, dl, p))
