
sum = 0
n,m,k = map(int,input("n,m,k 값 입력:").split())
array = list(map(int,input("array 값 입력:").split()))
array.sort(reverse=True)
data = [array[0],array[1]]
while m > 0:
    for i in range(k):
        if  m ==  0:
            break 
        else:
            sum += data[0]
            m -= 1
        print("sum",sum,"m",m, "first",data[0])
    if m == 0:
        break
    else:
        sum += data[1]
        m -= 1
    print("sum", sum, "m", m, "second", data[1])
print(sum)