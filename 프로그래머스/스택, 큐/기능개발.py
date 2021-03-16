r = [7,3,9]
count = 1
answer = []
while r:
    if len(r) == 1:
        answer.append(1)
        break
    else:
        y = r.pop(0)
    for x in r:
        if y >= x:
            r.remove(x)
            count += 1
        else:
            answer.append(count)
            count = 1
        print('y', y, 'x', x, 'r', r, 'count', count, 'answer', answer)

