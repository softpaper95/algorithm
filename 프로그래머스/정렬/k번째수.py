import heapq
array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
answer = []
for c in commands:
    i, j, k = c # i, j, k = c[0], c[1], c[2] 할필요 없이 저렇게 하면 된다.
    print(i, j, k)
    # 자르기
    temp = array[(i-1):j]
    # 정렬
    temp2 = []
    for t in temp:
        heapq.heappush(temp2, t)

    #k번째 숫자 구하기
    for n in range(k):
        a = heapq.heappop(temp2)

    answer.append(a)


def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
