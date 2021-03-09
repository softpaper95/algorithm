from collections import defaultdict
genres = ["classic", "pop", "classic", "classic", "pop","classic","classic","pop","classic",'jazz']
plays = [500, 600, 150, 800, 2500,900,400,200,800,80]
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
dict_sort = sorted(songs_dict.items(), key=lambda x : x[1], reverse=True)
for z in dict_sort:
    iter = []
    iter = [x for x in songs if x[0]==z[0]]
    if len(iter) >=2:
        result.extend([iter[0][2],iter[1][2]])
    else:
        result.append(iter[0][2])
print(result)

# 정답제출용
def solution(genres, plays):
    from collections import defaultdict
    songs = []
    cnt = 0
    answer = []

    for x, y in zip(genres, plays):
        songs.append([x, y, cnt])
        cnt += 1
    songs.sort(key=lambda x: (x[0], x[1]), reverse=True)
    songs_dict = defaultdict(int)

    for k in songs:
        songs_dict[k[0]] += k[1]
    dict_sort = sorted(songs_dict.items(), key=lambda x: x[1], reverse=True)

    for z in dict_sort:
        iter = []
        iter = [x for x in songs if x[0] == z[0]]
        if len(iter) >= 2:
            answer.extend([iter[0][2], iter[1][2]])
        else:
            answer.append(iter[0][2])
    return answer