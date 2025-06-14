def main():
    N,M = map(int,input().split())
    S = [input() for _ in range(N)]
    minStores = N

    for bit in range(1<<N):
        covered = set()
        count = 0 #店の数を記録
        for i in range(N):
            if bit & (1 << i):
                count += 1
                for j in range(M):
                    if S[i][j] == "o":
                        covered.add(j)
        if len(covered) == M:
            minStores = min(minStores, count)
    print(minStores)

main()