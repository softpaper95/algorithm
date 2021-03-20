import heapq
list = [[1,2],[4,2],[3,8],[5,6]]
heap =[]
for i in list:
    heapq.heappush(heap,i)

num = heapq.heappop(heap)[1]

print(heap)
print(num)