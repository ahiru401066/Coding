def main():
    N = int(input())
    S = [input() for _ in range(N)]

    L = set()
    for i in range(N):
        for j in range(i+1,N):
            x = S[i] + S[j]
            y = S[j] + S[i]
            L.add(x)
            L.add(y)
    print(len(L))

main()