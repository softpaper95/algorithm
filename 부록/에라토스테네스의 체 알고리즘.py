import math
n = 50
answer = []

array = [True for i in range(n+1)]
for i in range(2, int(math.sqrt(n))+1 ):
    if array[i] == True:
        multiple = 2
        while i * multiple < n+1:
                array[i * multiple] = False
                multiple += 1

for j in range(2,n+1):
    if array[j]:
       print(j, end=',')
