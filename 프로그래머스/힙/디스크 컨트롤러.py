import heapq
nums = [[0,3],[1,9],[2,6],[3,7],[5,8],[6,2]]
heap = []
for num in nums:
    heapq.heappush(heap, num)






heapq.heapify(nums,lambda x: x[1])
print(nums)
nums.sort(key=lambda x: x[1])
print(nums)
enu = 0
sum = 0
p = nums.pop(0)
print(p)
print(nums)
for i in range(10):
    p = nums.pop(0)
    if enu >= p[0]:
        sum += (enu + p[1]) - p[0]
        enu += p[1]
    # else:











