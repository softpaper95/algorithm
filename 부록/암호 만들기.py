from itertools import combinations
vowels = ('a', 'e', 'i', 'o', 'u')
l, c = map(int, input().split(' ')) #l = 암호글자 갯수, c =  문자종류의 갯수

array = input().split(' ')
array.sort()
# 모든 경우의 수를 구하기(중복x => combination 이용)
for password in combinations(array, l):
    count = 0
    for i in password:
        if i in vowels: #각각의 password에 모음이 있는지 확인
            count += 1
    if count >= 1 and l - count >= 2: #count가 1이상이면 모음, 암호글자갯수(l) - 모음갯수(count) = 자음갯수
        print(' '.join(password))