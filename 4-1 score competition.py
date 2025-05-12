def score_competition():
    N = int(input())
    a_score = list(map(int, input().split()))
    b_score = list(map(int, input().split()))
    diff = []

    for i in range(N):
        diff.append(a_score[i]-b_score[i])
    
    return print(*diff)

score_competition()
