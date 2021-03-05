# Number,M = map(int,input('Number와 M입력').split())
# weight = list(map(int,input('무게입력').split()))
# set_weight = set(weight)
#
# sum_cases = Number * (Number-1)
# sum = 0
#
# for num in set_weight:
#     cnt = 0
#     cnt = weight.count(num)
#     sum += cnt * (cnt -1)
# answer = (sum_cases - sum)/2
# print(answer)

n, m = map(int,input().split())
data = list(map(int, input().split()))

array = [0] * 11 # data의 요소들의 갯수를 저장할 배열

for x in data:
    array[x] += 1  # data의 요소들의 수를 array에 저장시켜준다.

result = 0 # 초기값 세팅
for i in range(1, m+1):
    n -= array[i] # 전체(남은)경우의 수(n) - 공의 갯수(array[i])
    result += array[i] # result에 무게에 따른 경우의수 누적

print(result)
