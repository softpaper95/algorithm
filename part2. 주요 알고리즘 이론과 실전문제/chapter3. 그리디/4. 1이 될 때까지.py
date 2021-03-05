n,k = map(int,input("n과 m을 입력하시오").split())
count = 0
while n>1:
    if n%k != 0:
        value = n % k
        count += value
        n -= value
    else:
        n = n/k
        count += 1
print(count)