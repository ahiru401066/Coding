def main():
    N = int(input())
    S = [input() for _ in range(N)]

    L = [[i,0] for i in range(N+1)]; L[0][1] = -10000
    for i in range(N):
        for j in range(N):
            if S[i][j] == "-": break
            
            if S[i][j] == "o":
                L[i+1][1] += 1
                L[j+1][1] -= 1
            elif S[i][j] == "x":
                L[i+1][1] -= 1
                L[j+1][1] += 1
    L.sort(key=lambda x:x[1], reverse=True)
    print(*[l[0] for l in L[:-1]])
    # print(L)


main()