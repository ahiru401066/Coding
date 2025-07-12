def main():
    N,D = map(int,input().split())
    S = [input() for _ in range(N)]
    L = [True] * (D)
    for i in range(N):
        s = S[i]
        for j in range(D):
            if s[j] == "x":
                L[j] = False
    # print(L)
    maxlength = 0; length = 0
    for i in range(len(L)):
        if L[i]: length += 1
        else:
            maxlength = max(maxlength,length)
            length = 0
    else:
        maxlength = max(maxlength,length)
    print(maxlength)

main()