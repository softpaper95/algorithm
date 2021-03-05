
right = int(input("큰 숫자를 입력:"))
left = int(input("작은 숫자를 입력:"))
data = [10, 20, 30, 40, 50]
n = 5 #데이터의 갯수
data_sum = [0]
sum = 0

#data의 합들을 data_sum에 삽입
for i in data:
    sum += i
    data_sum.append(sum)

#P[R] - P[L -1]
result = data_sum[right] - data_sum[left - 1]

print(result)

