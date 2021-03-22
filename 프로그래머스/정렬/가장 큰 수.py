numbers = [0, 1, 0, 0, 0]

numbers = list(map(str, numbers))
numbers.sort(key = lambda x : x*3, reverse = True)

print(numbers)
print((''.join(numbers)))



# def change(numbers,x,y):
#     temp = 0
#     index_x = numbers.index(x)
#     index_y = numbers.index(y)
#     temp = numbers[index_x]
#     numbers[index_x] = numbers[index_y]
#     numbers[index_y] = temp
#
# for b in range(len(numbers)):
#     for x,y in zip(numbers, numbers[1:]):
#         X = str(x)
#         Y = str(y)
#         # X,Y가 몇의 자리 수인지 판단하기
#         if len(X) >= len(Y):
#             n = len(Y)
#         else:
#             n = len(X)
#         for i in range(n):
#             if X[i] < Y[i]:
#                 change(x,y)
#                 break
#             elif X[i] > Y[i]:
#                 break
#             else:   # X[i] == Y[i]
#                 if X in Y or Y in X:
#                     m = max(x,y)
#                     # print(m)
#                     if str(m)[i] < str(m)[i+1]:
#                         if m == x:
#                             break
#                         else:
#                             change(x,y)
#                     elif str(m)[i] > str(m)[i+1]:
#                         if m == x:
#                             change(x,y)
#                         else:
#                             break
# answer = str(numbers.pop(0))
# for num in numbers:
#     num = str(num)
#     answer += num
# print(answer)


# import heapq
# from collections import deque
# numbers = [3, 30, 34, 5, 9]
# temp = []
# answer = []
# deque_answer = deque(answer)
# answer = 0
# for z in numbers:
#     heapq.heappush(temp, str(z))
# for i in range(len(temp)):
#     deque_answer.appendleft(heapq.heappop(temp))
# x = deque_answer[0]
# for y in range(1, len(deque_answer)):
#     x += deque_answer[y]
# print(x)
# #실패 다시 시도할 것!