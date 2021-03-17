import time

def solution(priorities, location):
    answer = 0
    # priorities의 각 요소에 번호를 부여한다.
    p = [(x,y) for x,y in enumerate(priorities)]

    while True:

        v = p.pop(0)
        #v[1]보다 하나라도 큰 수가 있으면 v를 p의 맨 뒤로 보낸다.
        if any(v[1] < q[1] for q in p):
            p.append(v)
        else:
            #v[1]이 p에서 제일 크면 그 수에 번호(answer)를 부여한다.
            answer += 1
            #v의 index번호와 location이 일치할때의 순서번호(answer)를 return한다.
            if v[0] == location:
                return answer


start_vect=time.time()
print("training Runtime: %0.2f Minutes"%((time.time() - start_vect)/60))
