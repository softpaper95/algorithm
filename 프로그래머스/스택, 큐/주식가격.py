from collections import deque
prices = [2,3,1,1,1,2,2,2]
prices = deque(prices)
answer = []
# answer = [0] * len(prices)

for i in range(len(prices)-1):
    for j in range(i, len(prices)-1):
        if prices[i] >prices[j]:
            break
        else:
            answer[i] +=1
        print("prices", prices, 'answer', answer)
# print(answer)



while prices:
    temp = prices.popleft()
    count = 0
    for k in prices:
        if temp <= k:
            count += 1
        else:
            count += 1
            break
    answer.append(count)
    print('count',count,"prices",prices,'answer',answer)
#
