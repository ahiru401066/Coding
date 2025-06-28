def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))

    Scores = []; Questions = []
    for k in range(N):
        score = 0; li = []
        S = input()
        for i in range(M):
            if S[i] == "o": score += A[i]
            else: li.append(A[i])
        li.sort()
        Scores.append(score+(k+1))
        Questions.append(li)
    maxScore = max(Scores)
    # print(Scores)
    # print(Questions)

    for i in range(N):
        count = 0; score = Scores[i]
        while score < maxScore:
            score += Questions[i].pop() 
            count += 1
        print(count)

main()