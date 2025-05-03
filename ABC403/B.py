def main():
    n = int(input())
    li = list(map(int, input().split()))

    indexedScores = [(score, i) for i, score in enumerate(li)]

    indexedScores.sort(reverse=True)

    ranks = [0] * n
    r = 1; i = 0

    while i < n:
        currentScore = indexedScores[i][0]
        j = i
        while j < n and indexedScores[j][0] == currentScore:
            j += 1

        for k in range(i,j):
            personIndex = indexedScores[k][1]
            ranks[personIndex] = r
        
    r += (j - i)
    i = j

    for rank in ranks:
        print(rank)

main()