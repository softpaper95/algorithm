N = int(input("n의 숫자를 입력하세요"))
group = list(map(int,input("개인의 공포도를 입력하세요:").split()))
group.sort()
count = 0

for i in range(len(group)):
    try:
        if group[0] > len(group) or len(group) == 0:
            break
        else:
            group = group[group[0]: ]
            count += 1
            print('group:',group)
    except:
        pass
print(count)

