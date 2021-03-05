# numbers = list(map(int,input().split()))
listNumbers = str(input())
numbers = []
for i in range(0, len(listNumbers)):
    numbers.append(listNumbers[i])



sum = 0
for i in numbers:
    if int(i) == 0:
        sum += int(i)
    else:
        if sum == 0:
            sum += int(i)
        else:
            sum *= int(i)
print(sum)