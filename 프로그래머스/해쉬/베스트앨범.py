from collections import defaultdict
genres = ["classic", "pop", "classic", "classic", "pop","classic","classic","pop","classic",'jazz']
plays = [500, 600, 150, 800, 2500,900,400,200,800,80]
answer = []
# genres = set(genres)
# d = {e:[] for e in set(genres)}
# for i in zip(genres, plays, range(len(plays))):
#     d[i[0]].append([i[1],i[2]])
# genreSort =sorted(list(d.keys()), key= lambda x: sum(map(lambda y: y[0],d[x])), reverse = True)
#
# print(min(len(plays),2))
# print(genreSort)

songs = []
cnt = 0
result = []
for x,y in zip(genres,plays):
    songs.append([x,y,cnt])
    cnt += 1
songs.sort(key=lambda x: (x[0], x[1]),reverse=True)

songs_dict = defaultdict(int)
for k in songs:
    songs_dict[k[0]] += k[1]
print(songs_dict)
dict_sort = sorted(songs_dict.items(), key=lambda x : x[1], reverse=True)
for z in dict_sort:
    iter = []
    iter = [x for x in songs if x[0]==z[0]]
    if len(iter) >=2:
        result.extend([iter[0][2],iter[1][2]])
    else:
        result.append(iter[0][2])
# print(result)
#
# 정답제출용
def solution(genres, plays):
    from collections import defaultdict
    songs = []
    cnt = 0
    answer = []

    # songs[]에 genres,plays,고유번호를 넣는다.
    for x, y in zip(genres, plays):
        songs.append([x, y, cnt])
        cnt += 1
    # genres를 기준으로 정렬하되 plays를 순서대로 내림차순 정렬한다.
    songs.sort(key=lambda x: (x[0], x[1]), reverse=True)

    # default dic을 이용해 각 장르마다 plays의 합을 구한다.
    songs_dict = defaultdict(int)
    for k in songs:
        songs_dict[k[0]] += k[1]
    # plays를 기준으로 내림차순으로 장르를 구한다.
    dict_sort = sorted(songs_dict.items(), key=lambda x: x[1], reverse=True)

    # 장르에 만든 요소들을 iter에 넣은 후 2개의 고유숫자만을 answer에 입력시킨다.
    for z in dict_sort:
        iter = []
        iter = [x for x in songs if x[0] == z[0]]
        if len(iter) >= 2:
            answer.extend([iter[0][2], iter[1][2]])
        else:
            answer.append(iter[0][2])
    return answer