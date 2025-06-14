def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    if N == K+1:
        print(0)
        return
    
    totalMin = 10**10; total = 0
    for i in range(K+1):
        total = A[i+(N-K)-1] - A[i]
        totalMin = min(totalMin, total)
    print(totalMin)

main()
# 1個残りとその他残りで分ける