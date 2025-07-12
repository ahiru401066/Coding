def main():
    N = int(input())
    A = list(map(int,input().split()))
    A = [0] + A

    S = set(); pos = 1
    ans = []
    while True:
        S.add(pos)
        pos = A[pos]

        if pos in S:
            ans.append(pos)
            if len(ans) >= 2 and ans[0] == ans[-1]:
                print(len(ans[:-1]))
                print(*ans[:-1])
                return

main()