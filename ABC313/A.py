def main():
    N = int(input())
    P = list(map(int,input().split()))
    
    ans = 0
    p1 = P[0]
    for i in range(1,N):
        if p1 <= P[i]:
            ans = max(ans,P[i]+1-p1)
    print(ans)

main()