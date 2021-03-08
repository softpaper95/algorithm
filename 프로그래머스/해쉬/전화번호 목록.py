# 시도1
# def solution(phone_book):
#     answer = True
#     for i in range(1,len(phone_book)):
#         if phone_book[0] in phone_book[i]:
#             answer = False
#             break
#
#     return answer

# 시도2
a = [i for i in phone_book[0]]
for k in (1, len(phone_book)):
    count = 0
    b = [j for j in phone_book[k]]
    for x,y in zip(a,b):
        if x == y:
            count += 1
    if count == len(a):
        answer = False
        break
    else:
        answer = True


phone_book = ["119", "97674223", "1195524421"]
# 정렬을 하면 phone_book[0]의 값과 가장가까운 값이 순서대로 정렬되므로, 이 값의 앞과 뒤만 확인해주면 된다.
# ex) 정렬후 -> [119, 1195524421, 97674223] 이므로 zip으로 앞뒤 확인만 해주면 된다.

phone_book.sort()
answer = True
for x,y in zip(phone_book, phone_book[1:]):
    if x in y or y in x:
        answer = False
print(answer)

# 참고할것
# https://ychae-leah.tistory.com/47






