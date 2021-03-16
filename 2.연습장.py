import collections
import copy
progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
count = 1
answer = []
listX = []
progress = [(100-i) for i in progresses]
for x,y in zip(progress,speeds):
    if x%y == 0:
        listX.append(x//y)
    else:
        listX.append((x//y) + 1)

listX_deq = collections.deque(listX)

while listX_deq:
    y = listX_deq.popleft()
    print("y:",y)
    for i in copy.deepcopy(listX_deq):
        if y >= i:
            count += 1
            listX_deq.remove(i)
        else:
            answer.append(count)
            count = 1
            break
        print("y:",y,"listX_deq:",listX_deq,"i:",i,"count:",count,'answer:',answer)
if count > 1:
    answer.append(count)
else:
    answer.append(1)
print("y:",y,"listX_deq:",listX_deq,"count:",count,'answer:',answer)
