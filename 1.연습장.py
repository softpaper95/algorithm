import heapq
list = [1,2,3,10,9,12]
heapq.heapify(list)
for i in range(len(list)):
    i = heapq.heappop(list)
    print(i, end=' ')
