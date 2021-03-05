# 나의 답안
x = []
n,m = map(int,input("m,n의 값을 입력하시오").split())
value = 0

for i in range(n):
    data = list(map(int,input("data 값을 입력하시오 ").split()))
    x.append(data)
for j in range(len(x)):
    if value < min(x[j]):
        value = min(x[j])
print(value)


# 책 답안
result = 0
n,m = map(int,input("m,n의 값을 입력하시오").split())

for i in range(n):
    data = list(map(int,input("data 값을 입력하시오 ").split()))
    min_value = min(data)
    result = max(result,min_value)
print(result)