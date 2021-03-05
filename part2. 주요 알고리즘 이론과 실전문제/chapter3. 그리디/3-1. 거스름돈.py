count = 0
n = int(input())
change = [500, 100, 50, 10]

while n > 0:
    for i in change:
        if i <= n:
            l = n//i
            n = n - (i*l)
            count += l
print(count)
