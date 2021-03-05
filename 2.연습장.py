a = list(map(int,input().split()))
b = list(map(int,input().split()))
n = len(a)
m = len(b)
result = [0] * (n+m)
i = 0
j = 0
k = 0

# 모든 원소가 결과 리스트에 담길 때까지 반복
while i < n or j < m:
    #리스트 b가 마지막이거나, 리스트 b의 원소가 a의 원소보다 큰 경우
    if j>=m or (a[i] <= b[j] and i<n):
        result[k] = a[i]
        i += 1
    else:
        result[k] = b[j]
        j += 1
    k += 1

#결과 리스트 출력
for i in result:
    print(i, end=" ")
