def main():
    n = int(input())
    A = list(map(int, input().split()))
    sumA = sum(A)

    # 累積和
    preSum = [0] * (n+1)
    total = 0
    for i in range(len(A)):
        total += A[i]
        preSum[i+1] = total
    
    ans = 0
    for i in range(len(A)-1):
        ans += A[i] * (sumA - preSum[i+1])
    print(ans)


main()
#部分和かな？