def main():
    def bs(x):
        left = -1; right = len(A)
        while left + 1 < right:
            mid = (left+right)//2
            if A[mid] >= x: right = mid
            elif A[mid] < x: left = mid
        return left

    N,Q = map(int,input().split())
    A = list(map(int,input().split()))
    B = [int(input()) for _ in range(Q)]


    A.sort()
    maxA = max(A)
    preA = [A[0]]
    for i in range(1,len(A)):
        preA.append(preA[i-1]+A[i])

    # print(A)
    # print(preA)
    for b in B:
        if b > maxA:
            print(-1)
        elif b == 1: print(1)
        else:
            index = bs(b)
            if index == -1:
                print((b-1) * len(A) + 1)
            else:
                print(preA[index] + (b-1) * (len(A) - (index+1)) + 1)

main()

# 特殊ケースは1?
# ２分探索　境界
# 累積和

# 俺が個数を指定
# ディーラーがteaバックを個数分渡す

# 難易度が高い -> teaバックが複数種類になりやすい