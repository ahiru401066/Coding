def main():
    N = int(input())
    A = list(map(int,input().split()))
    R = 10**8

    cSum = [0]
    for i in range(N):
        cSum.append(cSum[i]+A[i])
    # print(cSum)
    
    total = 0
    for i in range(N-1):
        total += (N-i-1)*A[i]+(cSum[N]-cSum[i+1]) % R
    print(total % R)

main()
# 割って足す = 足して割る　だと助かる
# 累積和の実装遅い