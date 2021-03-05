import math
n = int(input("n의 값을 입력하시오:"))
m = int(input("m의 값을 입력하시오:"))
numbers = [True for i in range(n+1)]


for j in range(2, int(math.sqrt(n))+1):
    if numbers[j] == True:
        k = 2
        while j * k <= n:
            numbers[j * k] = False
            k += 1
for v in range(m, n):
    if numbers[v]:
        print(v)