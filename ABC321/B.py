def main():
    N,X = map(int,input().split())
    A = list(map(int,input().split()))

    ans = 101
    c = max(A)
    while c >= 0:
        B = [a for a in A]
        B.append(c)
        total = sum(B) - max(B) - min(B)
        if total >= X:
            ans = min(ans,c)
        c -= 1
    if ans == 101: print(-1)
    else: print(ans)

main()