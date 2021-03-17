import heapq

nums = [4,1,7,3,8,5]
heap = []
for num in nums:
    heapq.heappush(heap, (-num,num)) #(우선순위, 값)

while heap:
    print(heapq.heappop(heap)[1], end =' ')



# heap = [4,1,7,3,8,5]
# sorted_heap = []
# sorted_heap2 = []
# # for i in nums:
# #     heapq.heappush(heap,i)
# #     print(heap,i)
#
#
# # heapq.heapify(heap)
# while heap:
#     sorted_heap.append(heapq.heappop(heap))
#     print(sorted_heap, end=' ')
#
# while sorted_heap:
#     sorted_heap2.append(heapq.heappop(sorted_heap))
#     print(sorted_heap2)


# print(heap)
# while list:
#     i = heapq.heappop(list)
#     print(i)
#     heapq.heappush(x,i)
# print(x)