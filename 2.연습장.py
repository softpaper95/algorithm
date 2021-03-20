import heapq
from collections import deque
jobs = [[0, 3], [1, 9], [2, 6],[12,2]]
heap = []
now = 0
answer = 0

for job in jobs:
    heapq.heappush(heap, [job[1],job[0]])

while i < len(jobs):
    cur = heapq.heappop(heap)
    if cur[1] <= now:
        now += cur[0]
        answer += (now - cur[1])
    else:
        heap.append(cur)
        now += 1
