# 원리
# 경우의 수는 (옷종류의 갯수 + 1) * (모자종류의 갯수 + 1) * (신발종류의 갯수 + 1) -1 이다.
# +1을 해주는 이유는 종류마다 아무것도 안입을 경우때문이고 ex)옷과 모자는 안입고 신발만 입는다. -> 이 경우에는 신발의 옷과 모자는 안입는 경우의 수가 하나 +1이다.
# 마지막에 -1을 해주는 이유는 아무것도 안입는 경우는 없기 때문이다.


# def solution(clothes):
#     # clothes를 [1]을 기준으로 정렬한다.
#     clothes_sort = sorted(clothes, key=lambda x: x[1])
#     answer = 1
#     count = 1
#
#     # clothes의 요소들을 앞뒤로 비교한다.
#     for x, y in zip(clothes_sort, clothes_sort[1:]):
#         # 앞뒤의 요소가 같다면 count로 수를 센다.
#         if x[1] == y[1]:
#             count += 1
#         #앞뒤가 다르다면 종류가 다르다는 뜻이므로 경우의 수를 곱해준다.
#         else:
#             answer *= count + 1
#             # count를 초기화 해준다.
#             count = 1
#     # 만약에 마지막 값의 앞뒤가 같지않다면 answer *= count + 1를 못해줌으로 한번더 적어주고 최종결과값에 -1을 해줌으로써
#     # 모두 벗는 경우의수는 제거해준다.
#     answer = answer * (count + 1) - 1
#     return answer

# 다른사람의 풀이
# reduce 이용
# reduce 개념 설명: https://www.daleseo.com/python-functools-reduce/
