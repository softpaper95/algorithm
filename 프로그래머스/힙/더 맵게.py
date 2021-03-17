import heapq

scoville = [1,2,3,10,9,12]
k = 7



print(deq_scoville)

def solution(scoville, k):
    heapq.heapify(scoville)
    answer = 0
    while scoville[0] < k:
        # 왜 while scoville로 하면 안될까????? -> 런타임 오류 뜸
        if len(scoville) > 1:
            new = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
            heapq.heappush(scoville,new)
            answer += 1
        else:
            return -1
    return answer


