import heapq
jobs = [[0, 3], [1, 9], [2, 6]]
import heapq

#
# def solution(jobs):
answer, now, i = 0, 0, 0
heap = []

while i < len(jobs):
    for job in jobs:
        if now >= job[0]:
            heapq.heappush(heap, (job[1], job[0]))

    if len(heap) > 0:
        cur = heapq.heappop(heap)
        now += cur[0]
        answer += (now - cur[1])
        i += 1
    else:
        now += 1
    print('heap:',heap,'cur:',cur,'now:',now,'answer:',answer,"i:",i)
print( int(answer / len(jobs)) )


