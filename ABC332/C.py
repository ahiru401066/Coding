def main():
    N,M = map(int,input().split())
    S = input()

    total = 0
    m = M; l = 0
    for i in range(len(S)):
        if S[i] == "0":
            total = max(total, -l)
            m = M; l = 0
        elif S[i] == "1":
            if m > 0: m -= 1
            else: l -= 1
        elif S[i] == "2":
            l -= 1
    total = max(total, -l)
    print(total)

main()