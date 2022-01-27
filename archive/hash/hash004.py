def solution(genres, plays):
    rank_genre = {}
    genre_arr = {}
    answer = []

    for i in list(set(genres)):
        rank_genre[i] = 0
        genre_arr[i] = []

    for i in range(len(genres)):
        rank_genre[genres[i]] += plays[i]
        genre_arr[genres[i]].append(plays[i])

    rank = []
    for i in sorted(rank_genre.items(), key=lambda it:(it[1], it[0]), reverse=True):
        rank.append(i[0])

    for i in rank:
        cnt = 0
        genre_arr[i].sort(reverse=True)
        for j in genre_arr[i]:
            if cnt == 2:
                break
            if plays.index(j) in answer:
                start = plays.index(j)
                print(start)
                answer.append(plays.index(j, start+1))
            else :
                answer.append(plays.index(j))
            cnt += 1
    return answer

print(solution(genres, plays))