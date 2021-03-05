n = int(input())
data = list(map(int,input().split()))
data.sort() # 오름차순으로 정렬한다. -> 요소를 차례대로 target과 비교하기 위해서이다.

target = 1 # 1부터 순서대로 coins의 요소와 비교하기위해 target의 초기값은 1로 설정한다.
for i in data:
    if target < i: # target보다 요소의 값이 더 크다면 그 수 는 만들 수 없는 수이므로 break를 통해 반복문을 탈출한다.
        break
    target += i # target이 요소의 값보다 크가나 같다면 그 수는 만들 수 있는 수이므로 coins요소를 target에 더하여 다음 수를 비교하도록 한다.

print(target)
